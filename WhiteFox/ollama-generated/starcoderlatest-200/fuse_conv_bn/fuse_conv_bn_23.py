
class ConvBatchNormModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        conv = torch.nn.Conv2d(...)
        bn  = torch.nn.BatchNorm2d(...)
        output = bn(conv(input_tensor))
        return output

class FcBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        fc = torch.nn.Linear(...)
        bn  = torch.nn.BatchNorm1d(...)
        output = bn(fc(input_tensor))
        return output


# Initializing the model
m = FcBnModel()

# Inputs to the model
x = torch.randn(1, 2048)
