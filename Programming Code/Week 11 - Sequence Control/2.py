def visitId(self, ctx, o):
  sym = next(filter(lambda x: x.name == ctx.name, o.sym), False)
  if o.isLeft:
    if type(sym.value) is Index:
      code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame)
    else:
      code = self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
  else:
    if type(sym.value) is Index:
      code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
    else:
      code = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
      
  typ = sym.mtype
  return code, typ