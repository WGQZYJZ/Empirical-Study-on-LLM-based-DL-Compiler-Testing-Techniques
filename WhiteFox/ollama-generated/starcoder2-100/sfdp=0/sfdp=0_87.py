
import torch
import torch.nn as nn
from typing import List, Tuple
 
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    @staticmethod
    def scaled_dot_product(query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> Tuple[torch.Tensor]:  # noqa
        