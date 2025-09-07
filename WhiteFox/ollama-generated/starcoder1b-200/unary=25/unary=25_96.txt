
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, -v1) # For each element in v1, if the corresponding element is True, choose the output of the linear transformation as the corresponding element from the linear transformation's output, otherwise choose a negative value from the output of the multiplication by the negative slope
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # The inputs should be positive
