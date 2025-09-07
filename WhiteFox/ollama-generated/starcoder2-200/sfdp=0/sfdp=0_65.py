
class Model(torch.nn.Module):
    def __init__(self, dim: int = 768) -> None:
        super().__init__()
 
        self.layer1  = torch.nn.Linear(dim, dim)
 
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        v20  = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(768)
 
        v30  = v20.softmax(dim=-1)
 
        return torch.matmul(v30, x1).tanh_()
