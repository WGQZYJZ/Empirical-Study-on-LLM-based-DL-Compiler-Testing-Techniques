
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Pointwise convolution
        v2 = v1 + torch.randn_like(v1) 
        v3 = F.relu(v2)  
        return v3


# Initializing the model
m  = Model()

# Input to the model
x1 = torch.randn(1, 3, 64, 64)
