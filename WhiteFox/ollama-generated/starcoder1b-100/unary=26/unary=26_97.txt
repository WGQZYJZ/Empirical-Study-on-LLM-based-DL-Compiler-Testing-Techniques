
class Model(nn.Module):
    def __init__(self, negative_slope: float = 0):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = F.conv2d(x1, kernel_size=(1, 1), stride=1, padding=0, bias=True) * self.negative_slope
        v2 = torch.where(v1 > 0, x1, -v1)
        return v2


# Initializing the model
m = Model()

