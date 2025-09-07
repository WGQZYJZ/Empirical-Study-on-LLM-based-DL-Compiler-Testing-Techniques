
class Model(torch.nn.Module):
    def __init__(self, l1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1


# Initializing the model with a list [5, 6] as the input to torch.nn.Conv2d:
m = Model([5, 6])
 
