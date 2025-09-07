
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(2, 3, 1)
        self.bn = torch.nn.BatchNormXd(3)

    def forward(self, x):
        v1 = torch.nn.functional.convNd(x, self.conv, bias=None)
        return torch.nn.functional.batch_norm(v1, self.bn.weight, None, 0., True, False).view(-1, 3)

# Initializing the model