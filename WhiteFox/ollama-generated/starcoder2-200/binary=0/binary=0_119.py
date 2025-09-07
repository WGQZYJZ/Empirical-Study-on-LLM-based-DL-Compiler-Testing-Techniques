
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + t2
        return v2


# Initializing the model with a random tensor to be added: t2
t2  = torch.randn(3, 8, 64, 64)
 
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

