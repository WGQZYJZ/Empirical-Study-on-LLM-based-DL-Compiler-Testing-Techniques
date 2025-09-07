 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(6)

    def forward(self, x1):
        conv_out = self.conv(x1)
        norm_out = self.bn(conv_out)
        return norm_out


# Initializing the model 
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 3, 5, 5)
