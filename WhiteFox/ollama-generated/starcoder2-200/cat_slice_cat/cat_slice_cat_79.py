
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1[:, 0:9223372036854775807]) 
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 1024, 512)
 
# Inputs to the model
x2 = torch.randn(96872, 5)
 
__output__  = m((torch.cat([x1[None], x2], dim=0)))

