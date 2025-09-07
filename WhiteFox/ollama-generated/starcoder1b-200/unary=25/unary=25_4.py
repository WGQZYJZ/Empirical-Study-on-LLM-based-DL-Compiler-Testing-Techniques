
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, 0.5 * negative_slope)  # For each element in v1, if the corresponding element is True, multiply it by the negative slope (and then choose t3 for the corresponding element). Otherwise, multiply t1 for the corresponding element
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4)
