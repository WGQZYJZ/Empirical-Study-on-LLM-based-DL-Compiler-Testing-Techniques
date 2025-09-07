
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  * 0.5
        v3  = (v1 + torch.pow(v1,3)) *  0.47 
        v4  = v3  * 0.9768593573306333  
        v5  = torch.tanh(v4)
        v6  = v2* (v5 + 1)
        return v6


# Initializing the model
m = Model()

