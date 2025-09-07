
import torch
from typing import Tuple, List
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inputs: List[torch.Tensor]) -> torch.Tensor:  # type: ignore[override]
        v1 = torch.split(inputs[0], [128, 64], dim=0)
        return torch.cat([v1[i * 2 + 1].view(-1, 3) for i in range((len(v1) // 2))], axis=-1)


