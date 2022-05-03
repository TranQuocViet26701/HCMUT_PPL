def visitAssign(self, ast, o):
  rc, rt = self.visit(ast.rhs, Access(o.frame, o.sym, False))
  self.emit.printout(rc)
  lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym , True))
  self.emit.printout(lc)