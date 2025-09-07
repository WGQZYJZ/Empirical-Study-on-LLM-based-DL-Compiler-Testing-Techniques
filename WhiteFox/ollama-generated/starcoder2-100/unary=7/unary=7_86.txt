
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 8, 7, stride=1, padding=3)
        self.pooling = torch.nn.MaxPool2d((1, 2), stride=(1, 2))
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.pooling(v2)
        return v3


# Initializing the model