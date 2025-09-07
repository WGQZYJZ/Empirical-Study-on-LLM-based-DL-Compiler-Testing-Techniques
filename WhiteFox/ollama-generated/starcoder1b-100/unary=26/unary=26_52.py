
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0  # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = -self.negative_slope * v1
        v4 = torch.where(v2, x1, v3)  # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v4


# Initializing the model
m = Model()


