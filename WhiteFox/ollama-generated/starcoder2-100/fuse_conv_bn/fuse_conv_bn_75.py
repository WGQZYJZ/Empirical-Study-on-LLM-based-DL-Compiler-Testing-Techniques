
class Model(torch.nn.Module):
    def __init__(self, X=2):
        super().__init__()
        self.conv = torch.nn.ConvNd(X)
        self.bn   = torch.nn.BatchNormNd(X)

    def forward(self, x1):
        v1  = self.conv(x1)
        return self.bn(v1)

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(20, X=3)

