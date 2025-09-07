
class Model(torch.nn.Module):
    def __init__(self, input_shape=[2]):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(*input_shape[0])

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1], dim=0)
        return v2


# Initializing the model
m = Model([4])


# Inputs to the model
x1 = torch.randn(3, 4, 64, 64)
x2 = torch.randn(3, 4, 64, 64)
