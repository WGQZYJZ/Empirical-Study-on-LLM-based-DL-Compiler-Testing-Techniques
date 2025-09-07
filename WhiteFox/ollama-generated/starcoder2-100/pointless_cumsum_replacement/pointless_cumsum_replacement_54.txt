
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = 4257 # Dummy
        v1  = v0  * -1 # Negate the elements of the tensor
        v2  = self.conv(x1)
        v3  = v2 + v1
        return v3


# Initializing the model