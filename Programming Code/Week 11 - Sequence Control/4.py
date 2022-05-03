def visitIf(self, ctx, o):
  ec, et = self.visit(ctx.expr, Access(o.frame, o.sym, False))
  self.emit.printout(ec)
  falseLabel = o.frame.getNewLabel()
  self.emit.printout(self.emit.emitIFFALSE(falseLabel, o.frame))
  self.visit(ctx.tstmt, o)
  if ctx.estmt:
    exitLabel = o.frame.getNewLabel()
    self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
    self.emit.printout(self.emit.emitLABEL(falseLabel, o.frame))
    self.visit(ctx.estmt, o)
    self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))
  else:
    self.emit.printout(self.emit.emitLABEL(falseLabel, o.frame))
  