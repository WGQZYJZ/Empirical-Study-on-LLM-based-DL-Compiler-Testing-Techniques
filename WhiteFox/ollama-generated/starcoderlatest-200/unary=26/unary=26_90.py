
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=16, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        t2 = v1 > 0
        t3 = v1 * -0.2
        v4 = torch.where(t2, v1, t3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
