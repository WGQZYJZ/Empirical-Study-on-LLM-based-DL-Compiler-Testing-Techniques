
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other  = torch.randn()
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + self.other   
        return F.relu6(v2)


# Initializing the model
m  = Model()
__output__  = m(torch.randn(1, 3, 80, 80))

