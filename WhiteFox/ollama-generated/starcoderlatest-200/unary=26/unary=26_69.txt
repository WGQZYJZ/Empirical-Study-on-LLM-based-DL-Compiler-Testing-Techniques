
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=2, output_padding=0)
        self.negative_slope = torch.randn(8, dtype=torch.float).unsqueeze(dim=0)
 
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = (v1 > 0).byte()
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 128, 128)
