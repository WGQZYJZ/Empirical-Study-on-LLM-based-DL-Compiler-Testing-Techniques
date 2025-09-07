
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose1d(3, 8, 7)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * 4 # Create a mask where each element is True if the corresponding element in v1 is greater than 0
        v3 = torch.where(v2, v1, -10 + v1) 
        return v3


# Initializing the model