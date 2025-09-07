
class Model(torch.nn.Module):
    def __init__(self, other: Any = torch.zeros((1,))):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) 
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other # Here, 'other' is the parameter of 'Model'. Please try to use another name instead of 'other'.
        return v2


# Initializing the model