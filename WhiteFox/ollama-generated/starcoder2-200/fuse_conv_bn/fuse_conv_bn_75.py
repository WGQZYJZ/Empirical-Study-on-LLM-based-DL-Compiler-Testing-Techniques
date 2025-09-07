class Model(torch.nn.Module):
    def __init__(self, channel: int):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(30, 40, 5)
        bn = torch.nn.BatchNorm2d(num_features=40)
        x = conv(x1) 
        y = bn(x) 
        return y
