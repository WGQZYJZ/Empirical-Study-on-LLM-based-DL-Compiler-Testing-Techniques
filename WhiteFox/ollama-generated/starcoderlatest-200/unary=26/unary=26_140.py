
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
        self.negative_slope = 0.1
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        mask = v1 > 0
        negative_slope = -self.negative_slope * (v1 == 0).float()
        masked_input = torch.where(mask, v1, negative_slope)
        return masked_input


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
