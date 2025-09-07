
class FusedModel(torch.nn.Module):
    def __init__(self, batchNormClass, convClass):
        super().__init__()
        self.conv = convClass(in_channels=10) 
        self.bn  = bnClass(num_features=20) # Use BN with num_features = 20

    def forward(self, x1):
        return self.bn(self.conv(x1))

fusedModel  = FusedModel()
__output__  = fusedModel(torch.randn(3, 10), torch.nn.Conv2d)

