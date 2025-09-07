
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.other = torch.nn.Parameter(0 * torch.ones(4))
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.other 
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
__output__  = m(x1)

