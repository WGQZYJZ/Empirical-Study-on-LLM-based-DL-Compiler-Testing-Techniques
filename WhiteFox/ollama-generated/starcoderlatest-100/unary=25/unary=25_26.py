
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0 # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v2 = v1 * negative_slope
        v3 = torch.where(v1, v1, v2)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
