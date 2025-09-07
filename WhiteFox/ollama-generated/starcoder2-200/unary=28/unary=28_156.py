
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0) 
        return v2


# Initializing the model with the default parameters
m = Model()

# Inputs to the model
x1 = torch.randn(32)


__output__  = m(x1)

