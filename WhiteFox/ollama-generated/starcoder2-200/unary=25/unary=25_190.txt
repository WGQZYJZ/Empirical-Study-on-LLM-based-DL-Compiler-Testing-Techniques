
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 12)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v3 = -1e-6 if not torch.any(v1) else 5e-7 
        v4 = negative_slope * v3
        v5 = torch.where(v1, v2, v4)
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8,)
__output__  = m(x1)


