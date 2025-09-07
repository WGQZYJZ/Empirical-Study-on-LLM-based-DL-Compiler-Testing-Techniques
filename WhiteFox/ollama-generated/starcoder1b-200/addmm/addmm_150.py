
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        return self._forward(x1, inp)

    def _forward(self, x1, inp):
        v1 = torch.mm(x1, inp)  # Perform matrix multiplication on two input tensors
        return v1 + inp


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
inp = torch.randn(2, 3, 64, 64)
