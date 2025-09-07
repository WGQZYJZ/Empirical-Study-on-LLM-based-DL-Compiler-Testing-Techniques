
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(1, 32, kernel_size=3, padding=1)
        self.bn1 = torch.nn.BatchNormXd(32)
        self.relu = torch.nn.ReLU()
        self.pool = torch.nn.MaxPool2d(2, 2)

    def forward(self, x):
        v = self.conv1(x)
        bn = self.bn1(v)
        relu = self.relu(bn)
        pooled_input = self.pool(relu)
        return pooled_input


# Initializing the model
m = Model()

