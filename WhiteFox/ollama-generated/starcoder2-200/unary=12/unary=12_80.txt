
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v0  = self.conv(x1)
        v1  = F.sigmoid(v0)
        v4  = v0 * v1
        return v4


# Initializing the model