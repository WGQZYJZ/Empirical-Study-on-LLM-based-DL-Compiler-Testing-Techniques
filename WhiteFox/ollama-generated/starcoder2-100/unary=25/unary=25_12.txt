
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.relu6(v1).clamp(min=0)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(2, 3, 8, 8)
 
__output__  = m(x1)
