
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8*64*64, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
other  = torch.randn(8*64*64, 3)
x1     = torch.randn(3, 8*64*64).reshape(-1, 3)
__output__    = m(x1)