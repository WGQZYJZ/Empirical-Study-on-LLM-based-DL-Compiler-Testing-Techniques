
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 4, stride=1, padding=0, output_padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        t2 = v1 > 0
        v3 = v1 * -0.1
        v4 = torch.where(t2, v1, v3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
