
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.neg_conv  = torch.nn.LeakyReLU(negative_slope)

    def forward(self, x1: Tensor):
        v1 = self.conv(x1)
        v2 = (v1  * 0.5).tanh()
        v3 = (v1  * 0.7071067811865476).tanh()
        v4 = self.neg_conv(v3)
        v5 = v4 * 0.25
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
