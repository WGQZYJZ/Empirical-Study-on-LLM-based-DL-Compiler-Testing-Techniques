
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=4)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 + torch.randn((100))

# Initializing the model
m = Model()


