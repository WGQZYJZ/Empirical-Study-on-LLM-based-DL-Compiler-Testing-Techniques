import torch
from torch import nn as nn
import sys

class Mixin:
    def __call__(self, *args):
        return super().__call__(*args)

    @torch.jit._overload_method(nn.Module)
    def foo(self, v1): ... # <-- THIS IS THE LINE THAT'S BROKEN FOR VALIDATION

    @torch.jit._overload_method(nn.Module)
    def foo(self, v1: int):  # <-- THIS IS NOT!
        return None


class Model(Mixin):
  def __init__(self):
      self = super().__init__()

  def foo(self, v2): 
      pass
    
m = Model()
