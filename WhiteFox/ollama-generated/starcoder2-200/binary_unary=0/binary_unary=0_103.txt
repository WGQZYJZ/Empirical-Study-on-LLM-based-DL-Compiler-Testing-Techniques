
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = torch.randn((4, 3, 64, 64))
 
    def forward(self, x):
        v0  = self.other + (x / 5)[:, None]
        v2  = torch.relu(v0)
 
        return v2


# Initializing the model
m  = Model()
__output__  = m((torch.randn(4,3,64,64)))

