
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v = torch.mm(x1, inp) + inp  # Perform matrix multiplication on two input tensors
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(1, 8, 1024, 768)
