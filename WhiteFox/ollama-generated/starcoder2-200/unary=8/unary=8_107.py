
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1,stride=1,padding=1)
    
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3 # Addition
        v3 = torch.clamp(v2, min=0, max=6) # clamp operation
        v4 = v1 * v3 # Multiplication
        v5 = v4 / 6 # Division 
        return v5


# Initializing the model
m = Model()
