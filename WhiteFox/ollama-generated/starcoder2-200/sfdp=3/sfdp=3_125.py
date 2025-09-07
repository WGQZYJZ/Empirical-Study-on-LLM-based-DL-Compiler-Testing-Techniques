
class Attention(torch.nn.Module):
    def __init__(self, scale=1e-4):
        super().__init__()
 
        # Scaling factor
        self.scale = scale
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor,
                dropout_p=0.) -> torch.Tensor:
 
         