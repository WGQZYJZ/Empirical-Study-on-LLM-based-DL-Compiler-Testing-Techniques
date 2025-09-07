
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(64*32*18, 50)
 
    def forward(self, x1): 
        v1 = self.linear(x1)

        v2 = v1 + other
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4, 64*32*18)
other = torch.rand(50)
 
