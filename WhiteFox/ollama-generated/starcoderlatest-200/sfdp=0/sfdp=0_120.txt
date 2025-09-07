
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk: torch.Tensor, inv_scale: float = 1e-5) -> torch.Tensor:
        