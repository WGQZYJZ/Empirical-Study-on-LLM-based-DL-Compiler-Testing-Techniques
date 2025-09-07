
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 8)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(4, 3) # The keyword argument "other" is used here to represent the tensor that will be added in addition to the output of self.linear().
