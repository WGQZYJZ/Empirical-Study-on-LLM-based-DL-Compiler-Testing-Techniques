
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, 0) # Matrix multiplication between input1 and zero tensor.
        v3 = torch.mm(v1, x2) # Matrix multiplication between the result of the first matrix multiplication and input2.
        return v3 + v3


m = Model()
__output__  = m(torch.randn(5, 6), torch.randn(784))

