
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([8, 64], 1, dtype=torch.float32)
 
    def forward(self, x1):
        v1 = torch.cumsum(x1, 1)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 64)
