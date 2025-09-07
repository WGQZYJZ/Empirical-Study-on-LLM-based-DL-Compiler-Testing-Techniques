
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(784, 20)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 + other # add another tensor to the output of linear transformation 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(50, 784)
__output__  = m(x1)

other = torch.randn(50, 784)

# Expected output (to compare with the obtained result):
tensor([[ 29.,  36.],
        [ -2.,   3.],
        [-33., -30.],
        ...

