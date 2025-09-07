
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=-7)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2  = v1 - other
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
other  = torch.randn(300).to(torch.device('cuda')) / (3**0.5)
__input__ = torch.rand((1, 8, 64 + other[0], 64))
 