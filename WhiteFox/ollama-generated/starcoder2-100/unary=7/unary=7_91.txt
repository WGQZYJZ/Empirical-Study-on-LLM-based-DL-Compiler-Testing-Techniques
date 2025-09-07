
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, padding=4, padding_mode='circular')
 
    def forward(self, x1):
        v1 = self.conv1(x1) + 3
        v2 = v1 - 6
        v3 = torch.relu(-v2) / 6
        return v3


m = Model()
__output__  = m(torch.randn(2, 3, 50, 50))

# Initializing the model

# Inputs to the model


