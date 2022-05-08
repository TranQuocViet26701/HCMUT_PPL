def visitWhile(self,ctx,o):
  o.frame.enterLoop()

  labelContinue = o.frame.getContinueLabel()
  labelBreak = o.frame.getBreakLabel()
  expCode, expType = self.visit(ctx.expr, Access(o.frame, o.sym, False, True))
  self.emit.printout(self.emit.emitLABEL(labelContinue, o.frame) + expCode + self.emit.emitIFFALSE(labelBreak, o.frame))
  self.visit(ctx.stmt, o)
  self.emit.printout(self.emit.emitGOTO(labelContinue,o.frame) + self.emit.emitLABEL(labelBreak, o.frame))
  
  o.frame.exitLoop()
  return None  

def visitWhile(self, ast, o):
  frame = o.frame
  frame.enterLoop()
  cntLabel, brkLabel = frame.getContinueLabel(), frame.getBreakLabel()
  self.emit.printout(self.emit.emitLABEL(cntLabel, frame))
  self.emit.printout(self.visit(ast.expr, Access(frame, o.sym, False))[0])
  self.emit.printout(self.emit.emitIFFALSE(brkLabel, frame))
  self.visit(ast.stmt, o)
  self.emit.printout(self.emit.emitGOTO(cntLabel, frame))
  self.emit.printout(self.emit.emitLABEL(brkLabel, frame))
  frame.exitLoop()
  
  