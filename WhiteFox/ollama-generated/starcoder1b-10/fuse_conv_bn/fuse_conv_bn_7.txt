
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, input_tensor):
        output  = self.bn(self.conv(input_tensor))
        return output


# Initializing the model
m  = Model()


