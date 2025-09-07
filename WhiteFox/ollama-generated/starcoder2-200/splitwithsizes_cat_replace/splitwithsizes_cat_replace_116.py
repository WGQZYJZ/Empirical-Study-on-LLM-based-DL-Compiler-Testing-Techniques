
class Model(torch.nn.Module):
    def __init__(self, shape1=(256,), shape2=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.conv0 = torch.nn.Conv2d(3, 4, 1)
 
        self.maxpool = torch.nn.MaxPool2d((shape1[0], shape1[0]), stride=None, padding=(0,), dilation=1, ceil_mode=True)
        self.linear0 = torch.nn.Linear(in_features=8*4*int(3/4)*int(768/5), out_features=shape2 if shape2 is not None else 9)
 
    def forward(self, x1):
        v1 = self.conv(x1)
 
        self.conv0()
        v2 = torch.split(v1, [3*4], dim=-1)[-1]
        v3 = torch.reshape(v2, (len(shape1), 8))
        v5 = self.maxpool(v3).flatten()
 
        return self.linear0(v5)

# Initializing the model