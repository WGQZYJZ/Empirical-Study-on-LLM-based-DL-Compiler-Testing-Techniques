
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, inp=None):
        if inp is None:
            x1 = torch.randn(1, 3, 64, 64)
        else:
            x1 = inp

        v1 = self.conv(x1)
        return v1
 
# Initializing the model
m = Model()

# Input to the model
