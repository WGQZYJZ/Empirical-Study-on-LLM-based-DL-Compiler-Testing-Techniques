
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = (v1 > 0).float() * -1 + 0.75
        v4  = torch.where(v2 == 0.75, v3, v2) 
        return v4 


# Initializing the model
m  = Model()


# Inputs to the model