
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.sigmoid(v1)
        return v2 * v1


# Initializing the model
m = Model()

# Inputs to the model
__input_1__ = torch.randn(64, 512) # __input_1__ is a 2D tensor of size (64x512). 
