
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v2 = torch.bmm(x1, self.linearA) # or torch.matmul(x1, self.linearA)
        v3  = x1.permute(0, 2, 1).bmm(y1) # or torch.matmul(self.linearA.weight, y1) (or x1.permute(0, 2, 1).matmul(y1))
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 4, 5) # or torch.randn((3, 8), ...) 
y1  = torch.randn(2, 7) # or torch.randn(3, 6) (or a different matrix size, but with the same shape 3 and 7)
__output__  = m(x1, y1)

