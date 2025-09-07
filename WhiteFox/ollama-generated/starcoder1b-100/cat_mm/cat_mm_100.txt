
class Model(torch.nn.Module):
    def __init__(self, channel_num=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(channel_num, channel_num*3, 1)
 
    def forward(self, x1, x2):
        y1  = torch.cat([x1, x1, ..., x1], dim=-1)
        y2  = self.conv(y1)
        return y2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
x2 = torch.randn(10, 10, 3, 3)
