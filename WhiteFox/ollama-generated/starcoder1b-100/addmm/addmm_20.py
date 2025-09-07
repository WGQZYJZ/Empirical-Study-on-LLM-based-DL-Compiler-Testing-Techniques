
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.mm = torch.nn.Linear(inp, inp)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        v2 = v1 + x2
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(inp_size, 1)
