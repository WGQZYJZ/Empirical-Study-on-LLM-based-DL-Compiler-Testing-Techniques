
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7, stride=2, padding=3)
        self.bn1 = torch.nn.BatchNorm2d(64)

    def forward(self, x):
        conv_out = self.conv1(x)
        bn_out   = self.bn1(conv_out)

        out = (conv_out + bn_out)/2
        
        return out

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3, 3, 28, 28)
