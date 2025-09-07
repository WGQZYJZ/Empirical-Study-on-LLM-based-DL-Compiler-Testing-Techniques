
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1  = torch.nn.BatchNorm2d(8)
        self.relu1 = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.bn2  = torch.nn.BatchNorm2d(16)
        self.relu2 = torch.nn.ReLU()
        self.maxpool = torch.nn.MaxPool2d((10,10))
 
    def forward(self, x):
        h = self.conv1(x)  # Input shape: [batch_size, channels, height, width]
        h = self.bn1(h)    # Input shape: [batch_size, 8, height, width]
        h = self.relu1(h)   # Input shape: [batch_size, 8, height, width]
        h = self.conv2(h)  # Input shape: [batch_size, 16, height/10, width/10]
        h = self.bn2(h)    # Input shape: [batch_size, 16, height/10, width/10]
        h = self.relu2(h)   # Input shape: [batch_size, 16, height/10, width/10]
        h = self.maxpool(h) # Input shape: [batch_size, 8, height/10, width/10]
        return h


# Inputs to the model
x  = torch.randn(1, 3, 20, 50)
