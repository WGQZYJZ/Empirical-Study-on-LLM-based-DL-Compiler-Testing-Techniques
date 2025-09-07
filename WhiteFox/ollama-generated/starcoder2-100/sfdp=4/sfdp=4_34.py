
from typing import Optional
import torch

class SelfAttention(torch.nn.Module):
    def __init__(self, query_size: int) -> None:
        super().__init__()

    def forward(
            self,
            query: torch.Tensor,
            key: torch.Tensor,
            value: torch.Tensor,
            attn_mask: Optional[torch.BoolTensor] = None,
    ) -> torch.Tensor:


attn  = SelfAttention(query)


 # Inputs to the model
