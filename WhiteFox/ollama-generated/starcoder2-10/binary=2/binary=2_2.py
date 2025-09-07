
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        if not other is None:
            self.other_tensor  = torch.zeros((3, 3), dtype=torch.int64)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other_tensor
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(32, 3, 64, 64)
 
__output__  = m(x1)

