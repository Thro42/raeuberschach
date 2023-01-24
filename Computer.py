from __future__ import annotations
from typing import TYPE_CHECKING
from BoardMap import BoardMap
if TYPE_CHECKING: 
    from Color import Color
if TYPE_CHECKING: 
    from Game import Game
from Piece import Piece
from numpy import * 
from copy import copy, deepcopy

from Player import Player

class Computer:
    def __init__(self, game: Game, player: Player, enemy: Player):
        self.game = game
        self.color = player.color
        self.player = player
        self.enemy = enemy
        self.maxDeep = 3

    def checkPieceMove(self, piece: Piece, place: str, map: BoardMap, deep: int):
        rate = 0
        rate = self.checkIfCanHit(place)
        fcol = map.getFieldColor(place)
        if fcol != "-" and fcol != piece.color_short:
            rate += (-6 / deep)
        else:
            ndeep = deep + 1
            bmap = deepcopy(map)
            pcopy = copy(piece)
            pcopy.setMap(bmap)
            bmap.clearFieldColor(pcopy.place)
            pcopy.setAlphaPos( place )
            bmap.setFieldColor(place, pcopy.color_short)
            pcopy.select(False)
            if ndeep > self.maxDeep:
                rate += (2 / (len(pcopy.possibleFields) + 1))
            else:
                fval = [0] * len(pcopy.possibleFields)
                fpos = 0
                for pf in pcopy.possibleFields:
                    fval[fpos] = self.checkPieceMove(pcopy, pf, bmap, ndeep)
                    fpos += 1
                rate += sum(fval)
        print("Field:",place,"-", rate)
        return rate

    def getHitRate(self, place: str):
        rate = 0
        for p in self.enemy.color.pieces:
            if p.place == place:
                if p.pieceName == "pawn":
                    rate = 8*2
                elif p.pieceName == "king":
                    rate = 6*2
                elif p.pieceName == "knight":
                    rate = 4*2
                elif p.pieceName == "rook":
                    rate = 2*2
                elif p.pieceName == "bishop":
                    rate = 2*2
        return rate + 1


    def checkIfCanHit(self, place: str):
        can_hit = 0
        for p in self.enemy.color.pieces:
            p.select(False)
            for field in p.possibleFields:
                if field == place:
                    can_hit += 10
        return can_hit

    def checkMove(self):
        deep = 1
        cbord = copy(self.game.board)
        pval = [0] * len(self.color.pieces)
        ppos = 0
        valmax = 0
        bestPiece = None
        bestField = ""
        for p in self.color.pieces:
            bmap = deepcopy(cbord.boardmap)
            cpiece = copy(p)
            cpiece.setMap(bmap)
            cpiece.select(False)
            fval = [0] * len(cpiece.possibleFields)
            fpos = 0
            for pf in cpiece.possibleFields:
                #print(fpos, fval)
                fcol = bmap.getFieldColor(pf)
                if fcol != "-" and fcol != p.color_short:
                    fval[fpos] = 4000
                    fval[fpos] *= self.getHitRate(pf)
                fval[fpos] += self.checkPieceMove(cpiece, pf, bmap, deep)
                fpos += 1
            pval[ppos] = sum(fval)
            if pval[ppos] > valmax:
                valmax = pval[ppos]
                bestPiece = p
                pmax = 0
                for n in range(0,len(fval)):
                    if fval[n] > pmax:
                        pmax = fval[n]
                        bestField = cpiece.possibleFields[n]
            ppos += 1
        if bestPiece != None:
            self.player.movePiece(bestPiece, bestField)
            self.game.whitePlay = True

    def loop(self):
        if self.game.whitePlay != True:
            self.checkMove()
