
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1, x2=None):
        v1 = self.linear(x1)
        if x2 is not None:
            return v1 + x2
        else:
            return v1


# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(3, 4) # Input tensor for the model
