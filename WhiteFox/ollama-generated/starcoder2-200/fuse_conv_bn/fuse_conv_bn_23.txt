
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(2, 3)

    def forward(self, x):
        v0 = torch.nn.functional.convXd(x, conv1, stride=2, padding=[2])
        v1 = torch.nn.functional.batch_norm(v0, conv1.weight, conv1.bias, 0.1)

m = Model()

