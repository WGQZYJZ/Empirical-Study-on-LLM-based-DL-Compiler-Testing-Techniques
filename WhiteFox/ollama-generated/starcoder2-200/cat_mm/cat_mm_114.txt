
class Model(torch.nn.Module):
    def __init__(self, l1=[1], l2=[], l3=[]):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0 = self.conv(x1)
        v1  = torch.mm(v0, l1) 
        v2  = torch.cat([v1] + [torch.mean(l3)] * len(l1))
        return v2

# Initializing the model
m = Model()

