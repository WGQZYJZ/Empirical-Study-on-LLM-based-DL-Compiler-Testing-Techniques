
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(64, 256)
        self.linear2  = torch.nn.Linear(256, 783)
        self.conv  = torch.nn.Conv2d(783, 900, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.linear1(x)
        v2  = v1 + 5 
        v3  = self.linear2(v2) 
        v4  = torch.cat([v3], 0)
        v5  = self.conv(v4)
 
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 28*28) 
 
__output__  = m(x1)


