
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64*128, 3)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = torch.sigmoid(v1)
        v3  = v2 * v1
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 64*128).reshape(-1, 64*128)
__output__  = m(x)

