
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        s1 = v1[:, :5]
        t1 = v1[:, 5:24]
        s2 = torch.cat([s1, t1], dim=1)
        s3 = s2[:, :127]
        t2 = s2[:, 127:]
        return t2

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
