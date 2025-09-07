
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.where(v1 > 0, v1, -v1)  # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = v1 * negative_slope
        return v3


# Initializing the model
m = Model()


