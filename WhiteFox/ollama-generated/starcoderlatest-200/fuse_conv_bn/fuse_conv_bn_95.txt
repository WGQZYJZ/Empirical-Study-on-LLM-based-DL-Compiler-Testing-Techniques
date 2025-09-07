
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        out = F.relu(self.conv(x)) # ReLU applied before the batch norm layer (instead of after). The reason is that bn has a different channel dimension compared to conv. 
        return self.bn(out)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 6, 3)
