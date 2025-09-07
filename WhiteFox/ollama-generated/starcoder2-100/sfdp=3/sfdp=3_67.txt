
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1 / math.sqrt(d_k)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask=None, dropout: float = 0.0) ->torch.Tensor:
        