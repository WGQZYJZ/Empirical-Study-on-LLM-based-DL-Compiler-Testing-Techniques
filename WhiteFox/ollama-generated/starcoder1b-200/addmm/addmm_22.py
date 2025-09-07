
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, x2) + inp # Perform matrix multiplication on two input tensors
        return v1


# Inputs to the model
x1 = torch.randn(3, 4)
inp = torch.randn(2, 4)
