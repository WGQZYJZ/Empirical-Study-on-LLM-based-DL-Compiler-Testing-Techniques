
class Model(torch.nn.Module):
    def __init__(self, inp: torch.tensor):
        super().__init__()
        self.inp = inp
 
    def forward(self, x1):
        y = torch.mm(x1, self.inp) + self.inp  # Perform matrix multiplication on two input tensors
        return y


# Inputs to the model
inp = torch.randn(3, 3)  # Input of a tensor (a scalar is also accepted as a valid input)
