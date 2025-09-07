
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = (v1 > 0).float() # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        negative_slope = -2.0
        t3 = v1 * negative_slope
        t4 = torch.where(t1, v1, t3) 
        return t4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
