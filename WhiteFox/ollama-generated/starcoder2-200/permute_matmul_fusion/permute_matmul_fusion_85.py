class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1: torch.Tensor) -> torch.Tensor:
      return self._forward(t1)
    
    def _forward(self, x1):
        v1  = x1.permute([0, 2, 1]) 
        v2  = torch.bmm(v1, self.linear.weight, self.linear.bias) # or torch.matmul(v1, self.linear.weight, self.linear.bias)
        return v2
