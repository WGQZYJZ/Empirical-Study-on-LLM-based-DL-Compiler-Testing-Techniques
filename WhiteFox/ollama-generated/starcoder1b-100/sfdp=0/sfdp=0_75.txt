
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 1)
        self.conv2 = torch.nn.Conv2d(64, 64, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = torch.matmul(v1, v2) / torch.sqrt(torch.trace(v2 @ v2).reshape(-1, 1)) # Scaled dot-product attention mechanism
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(1, 64, 64)
