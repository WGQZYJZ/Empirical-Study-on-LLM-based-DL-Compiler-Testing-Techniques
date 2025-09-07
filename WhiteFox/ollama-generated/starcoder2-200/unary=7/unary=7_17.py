
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * F.clamp(min=0, max=6, input=v1 + 3)
        return v2 / 6

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(5, 32)
 
__output__  = m(x1)

