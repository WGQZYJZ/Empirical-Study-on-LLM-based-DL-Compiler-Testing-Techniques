
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*8 * 16, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2) # Other is a non-negative tensor that is added to the output of the linear transformation
        return v3


# Initializing the model
m  = Model()
other  = torch.randn(1, 10)

# Input for the model
x1  = torch.rand(2, 8*32 * 16)
__output__  = m(x1)

