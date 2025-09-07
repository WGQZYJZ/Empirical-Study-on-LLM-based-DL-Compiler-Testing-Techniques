
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=(64, 64), stride=(64, 64))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v2 = torch.gt(v1, torch.tensor(0.0).to(v1))
        v3 = v1 * -0.125
        # Apply the where function to select elements from v1 or v3 based on the mask v2
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
