
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(512 * 7, 3)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = F.sigmoid(v1)
        v3  = v1 * v2 # Applying sigmoid after multiplying
        return v3


# Initializing the model
m  = Model()
 

# Inputs to the model
x1  = torch.randn(64, 512 * 7)
 
# Forward pass of the model
