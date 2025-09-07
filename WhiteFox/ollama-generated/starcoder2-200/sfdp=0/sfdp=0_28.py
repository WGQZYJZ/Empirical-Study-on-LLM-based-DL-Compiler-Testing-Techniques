
import torch.nn as nn
from torch import Tensor
import math
 
class ScaledDotProductAttention(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.softmax = nn.Softmax(-1)
 
    @staticmethod
    def scaled_dot_product(query: Tensor, key: Tensor) -> Tensor:
        return torch.einsum('b n d c, b m l e, b o l d -> b o l c',
                             query / math.sqrt(key.shape[-2]), key, torch.ones_like(key))
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tuple[Tensor]:
        inv_scale = self.__inv_scale__(query=query, key=key)
 
        scaled_dot_product = ScaledDotProductAttention.scaled_dot_product(
            query=query / math.sqrt(query.shape[-2]),
            key=key / math.sqrt(query.shape[-2]))
        attention_weights = self.softmax(scaled_dot_product * inv_scale)
 
        output = torch.einsum('b o l c, b o l d -> b n d c',
                              attention_weights, value).contiguous()
 
        return output

    def __inv_scale__(self, query: Tensor, key: Tensor) -> Tensor:
        inv_scale = torch.sqrt(query.shape[-2])  # type: ignore
 

        return inv_scale