
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)
        self.bn1 = torch.nn.BatchNorm2d(...)
        self.pool = torch.nn.MaxPool2d(...)

    def forward(self, x):
        output = torch.nn.functional.batch_norm(...)
        return self.pool(torch.nn.functional.conv2d(...))

# Initializing the model
m = Model()
x = torch.randn(1, 3, 48, 60)
