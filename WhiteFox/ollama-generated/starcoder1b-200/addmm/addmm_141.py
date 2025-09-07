
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1: torch.Tensor, inp: torch.Tensor) -> torch.Tensor:
        return torch.mm(x1, inp)

 # Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
inp = torch.randn(2, 8, 64, 64)
