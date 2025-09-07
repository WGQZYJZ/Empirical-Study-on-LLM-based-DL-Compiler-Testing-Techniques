
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 1024)
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.where(v >= 0.,  v, negative_slope*v) # Where the output of the linear transformation is greater than or equal to 0.0 and less than 0.0, apply a negative slope * the corresponding element from the linear transformation.
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(10, 4096)
