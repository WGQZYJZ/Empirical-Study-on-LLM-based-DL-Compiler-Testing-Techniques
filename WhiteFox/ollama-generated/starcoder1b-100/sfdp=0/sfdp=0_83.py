
class ScaledDotProduct(nn.Module):
    def __init__(self, inv_dim):
        super().__init__()
        self.inv_dim = inv_dim
 
    def forward(self, query: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
        