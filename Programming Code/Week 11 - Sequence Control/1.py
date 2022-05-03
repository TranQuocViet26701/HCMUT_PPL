def visitVarDecl(self, ctx, o):
  if o.frame is None: 
    self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False))
    return Symbol(ctx.name, ctx.typ, CName(self.className))
  else:
    idx = o.frame.getNewIndex()
    self.emit.printout(self.emit.emitVAR(idx, ctx.name, ctx.typ, o.frame.getStartLabel(), o.frame.getEndLabel()))
    return Symbol(ctx.name, ctx.typ, Index(idx))
    