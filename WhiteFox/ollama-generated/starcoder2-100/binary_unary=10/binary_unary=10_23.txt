
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*3, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2) 
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
other  = torch.randn(10, dtype=torch.float32) 
x1     = torch.randn(5, 3, 32, 32)
__output__  = m(x1)