
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * -1  # Negative slope is chosen as (-1). If negative_slope < 0, then the corresponding element in t1 is multiplied by negative_slope to produce a positive value, and this result becomes v1.
        v4 = torch.where(v2, x1, v3)  # For each element in v2, if the element is True, choose the corresponding element from x1, otherwise choose the corresponding element from v3
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10)
