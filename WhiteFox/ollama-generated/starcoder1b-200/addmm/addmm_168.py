
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.bn1   = nn.BatchNorm2d(16)
        self.bn2   = nn.BatchNorm2d(16)
 
    def forward(self, x1):
        # Calculate the output from two convolutions
        v1 = F.relu(self.conv1(x1))
        v2 = F.relu(self.conv2(v1))
 
        # Calculate batch-mean for each channel separately
        # and then combine into one vector for later multiplication with another tensor
        v3 = torch.mean(torch.mean(v2, dim=1), dim=0)
        v4  = self.bn1(v2 + inp)
        v5  = self.conv2(v1)
        v6  = self.bn2(v4 + v5)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
