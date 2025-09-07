
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * torch.clamp(min=0, max=6, input=v1 + 3).to(dtype=torch.float32)
        v3 = v2 / 6
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50000, 10)
__output__  = m(x1)