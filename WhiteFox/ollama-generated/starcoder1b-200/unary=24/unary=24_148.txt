
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1 * 0.5, v1 * -1e-6)  # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = v1 * -0.7071067811865476
        v4 = torch.where(v2, v1, v3) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
