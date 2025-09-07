
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, input_tensor):
        conv = self.conv(input_tensor)
        output = self.bn(conv)
        return output
