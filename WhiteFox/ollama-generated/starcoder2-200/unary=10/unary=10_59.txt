
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v1 = self.linear(x) 
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6 # This is the scaled and shifted ReLU6 activation function
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 10)
__output__  = m(x1)

