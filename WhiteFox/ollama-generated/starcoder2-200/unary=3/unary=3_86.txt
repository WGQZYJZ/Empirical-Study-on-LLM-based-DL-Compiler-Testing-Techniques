
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5  
        v3  = v1 + torch.nn.functional.pad(v1, (0, 1), mode='constant', value=7.)  
        v4  = torch.erf(v3)  
        v5  = v4 + 1  
        v6  = v2 * v5
        return v6


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 70, 70)
