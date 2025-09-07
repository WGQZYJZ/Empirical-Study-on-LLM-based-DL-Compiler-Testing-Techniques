
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3)

 # Initializing the input tensor (The dimensions of this tensor must match the dimensions required by your linear transformation.)
x2 = torch.rand(8, 3)
 
 