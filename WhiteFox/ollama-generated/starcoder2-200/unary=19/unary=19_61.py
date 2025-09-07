
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 8 * 8 + 1, 3)
 
    def forward(self, x1):
        v0 = x1.reshape(-1, 256 * 8 * 8).contiguous()
        v1 = self.linear(v0)
        return torch.sigmoid(v1)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(327, 256*8*8+1).contiguous()
__output__  = m(x1)

