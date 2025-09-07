
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.inp = inp
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        v2 = v1 + self.inp
        return v2


# Inputs to the model
input1  = torch.randn(4, 8, 64, 64)
input2  = torch.randn(4, 3, 64, 64)
