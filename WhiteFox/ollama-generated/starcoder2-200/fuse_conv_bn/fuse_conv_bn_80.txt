
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1) # 1-dimensional conv
        return x1 * 0


# Initializing the model