
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(x1)
        v2  = self.conv2(v1) # Conv is here, which you don't want
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 50)

# Running the model on inputs
