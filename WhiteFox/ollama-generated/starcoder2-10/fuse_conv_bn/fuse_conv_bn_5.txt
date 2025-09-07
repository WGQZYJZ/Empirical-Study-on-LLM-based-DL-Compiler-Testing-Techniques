

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd()
        self.bn = torch.nn.BatchNormXd()

    def forward(self, input_tensor):
        bn  = self.bn(input) # Assuming the conv/bn layer is in training mode and is tracking running stats.
        output  = torch.nn.functional.conv_bn(x1, conv, bn) # Fuse the Conv/BN layer, removing BN.
        return output

m  = Model()


x1  = torch.randn(2, 3, 4)
