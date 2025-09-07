
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.fc   = torch.nn.Linear(8*64*64, 10)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.view(v1.shape[0], -1)
        v3 = self.fc(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
