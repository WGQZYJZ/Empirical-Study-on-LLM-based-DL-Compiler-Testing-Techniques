
class Model(torch.nn.Module):
    def __init__(self, kernel_size=2, padding=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=kernel_size, stride=1, padding=padding)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, 0], dim=1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
