
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(2, 2)

    def forward(self, x1):
        v1 = self.conv1(x1)  # apply convolution layer
        return v1
m = Model()
