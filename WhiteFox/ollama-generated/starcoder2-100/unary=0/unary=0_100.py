
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 + torch.pow(v1, 3.) *  0.7978845608028654 / (torch.exp(- torch.pow(v1, 3.)) + 1.)
        return v3


# Initializing the model
m = Model()
 
