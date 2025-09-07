
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.pool1 = torch.nn.AdaptiveAvgPool2d((1, 1))
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x):
        v = torch.nn.functional.avg_pool2d(x, 1)
        return self.conv1(v).view(-1, 3, v.shape[0], v.shape[2])


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
