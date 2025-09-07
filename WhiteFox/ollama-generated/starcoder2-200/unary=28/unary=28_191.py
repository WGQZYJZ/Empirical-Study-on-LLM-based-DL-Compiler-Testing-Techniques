
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = self.linear(x)
        v2  = torch.clamp_min(v1, -500.) 
        v3  = torch.clamp_max(v2,  4987.)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(batch)
__output__  = m(x1)

