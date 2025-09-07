

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
    
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()
other  = torch.randn(v1.shape) # Random tensor of same shape as v1

# Inputs to the model
x1  = torch.randn(3, 32) # 3x32 random matrix
__output__  = m(x1, other=other)
