
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=2)
        self.negative_slope = torch.nn.Parameter(-0.01)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        t1 = v1 > 0
        t2 = v1 * -0.01
        return torch.where(t1, v1, t2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 128, 128)
