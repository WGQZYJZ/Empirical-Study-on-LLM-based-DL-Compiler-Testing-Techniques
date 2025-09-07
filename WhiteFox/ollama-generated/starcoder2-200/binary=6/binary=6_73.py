
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8192, 3)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2

# Initializing the model and initializing 'other' to be non-zero
m  = Model()
o = torch.ones([8192]) * 0.5


# Inputs to the model
x1 = torch.randn(3, 64)
