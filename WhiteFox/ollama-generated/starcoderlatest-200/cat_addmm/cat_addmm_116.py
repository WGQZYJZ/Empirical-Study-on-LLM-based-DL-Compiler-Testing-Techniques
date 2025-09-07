
class Model(torch.nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.pool = torch.nn.MaxPool2d(2, stride=2)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.pool(v1)
        v3 = self.conv2(v2)
        return v3
 
# Initializing the model
m = Model(num_classes=10)

 # Inputs to the model
 x = torch.randn(1, 3, 64, 64) 
 