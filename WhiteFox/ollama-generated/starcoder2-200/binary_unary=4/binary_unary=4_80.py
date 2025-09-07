
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 5)
 
    def forward(self, x1, x2=None):
        v1  = self.lin(x1)
        if x2 is not None:
            v1 += x2 # Add an extra input tensor to the output of linear transformation
        return torch.relu(v1)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(5, 10)
x2 = torch.randn(5, 1)

# Calling forward
__output__  = m(x1, x2=x2).mean()
