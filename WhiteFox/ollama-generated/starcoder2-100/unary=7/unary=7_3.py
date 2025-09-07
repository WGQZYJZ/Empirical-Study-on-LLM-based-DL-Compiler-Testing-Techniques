
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=4, stride=2)
 
    def forward(self, x1):
        v0 = self.conv1(x1)
        return v0


# Initializing the model