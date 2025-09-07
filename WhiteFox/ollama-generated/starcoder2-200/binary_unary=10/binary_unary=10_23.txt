
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(32*32*8, 10)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + other  # The tensor that is not an input to the model
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
 

# Inputs to the model
x1  = torch.randn(1, 64*64*8)


