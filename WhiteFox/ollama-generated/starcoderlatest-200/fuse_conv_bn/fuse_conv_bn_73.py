
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = conv(x1)  # Replace 'conv' with functional API if the user chooses to use it instead of module API
        v2 = bn(v1)   # Replace 'bn' with functional API if the user chooses to use it instead of module API
#        