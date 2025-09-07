
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1: torch.Tensor, t2: torch.Tensor, arg1=1):
        t3 = torch.cumsum(t2, 1)
        return t3

# Inputs to the model
t1 = torch.randn(1, 4, 8, 8)
t2 = torch.randn(1, 3, 8, 8)
