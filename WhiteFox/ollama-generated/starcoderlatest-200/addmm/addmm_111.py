
class Model(torch.nn.Module):
    def __init__(self, inp_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(inp_dim, inp_dim)
 
    def forward(self, x1, input2):
        v1 = self.conv(x1)
        v2 = torch.mm(input1, input2) + inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v6


# Initializing the model
m = Model()


## please fill out following function inputs
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
input2  = torch.randn(1, 10)
