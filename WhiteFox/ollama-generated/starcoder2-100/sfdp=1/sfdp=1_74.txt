
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of two tensors
        return v


m  = Model()

x1  = torch.randn(48)
x2  = torch.randn(3056, 9672).float()
__output__  = m(x1, x2)

