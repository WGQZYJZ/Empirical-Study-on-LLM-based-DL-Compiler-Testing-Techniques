import torch
from torch import nn

def drop_path(x, drop_prob: float = 0., training: bool = False):
    