
class Model(torch.nn.Module):
    def __init__(self, inp: Tensor)
        super().__init__()
        self.inp = inp
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        v2 = v1 + self.inp
        return v2


# Initializing the model
m = Model(__input__)


# Inputs to the model
__input__ = torch.randn(1, 3, 64, 64)
x1 = torch.randn(1, 3, 64, 64)
