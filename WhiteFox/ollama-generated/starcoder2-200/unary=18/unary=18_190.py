
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8, 1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v1 = torch.sigmoid(v0)
        return v1


# Initializing the model