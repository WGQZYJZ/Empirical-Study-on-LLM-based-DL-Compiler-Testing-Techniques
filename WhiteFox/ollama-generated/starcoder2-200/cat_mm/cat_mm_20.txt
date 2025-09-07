
class Model(torch.nn.Module):
    def __init__(self, l1: List[int], l2: List[float]):
        super().__init__()
 
    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
 
        v3 = torch.cat([v1, v2], 0)
        return v4


# Initializing the model
l1  = [1] * 5
l2  = [2.] * 7
 
m  = Model(l1=l1, l2=l2)


# Inputs to the model
x3  = torch.randn(5, 4096)
x4  = torch.randn(7, 8192)
__output__  = m(x3, x4)


