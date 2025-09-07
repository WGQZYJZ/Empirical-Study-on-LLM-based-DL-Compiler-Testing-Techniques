
class Model(torch.nn.Module):
    def __init__(self, d_in: int, d_out: int):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(d_in, 32, 4, stride=2, padding=0)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(32, 32, 4, stride=2, padding=1)
        self.batch_norm1 = BatchNorm1D()
        self.relu2 = torch.nn.ReLU()
        self.maxpool = torch.nn.MaxPool2d((2, 2))
        self.conv3 = torch.nn.Conv2d(32, d_out, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.relu(self.batch_norm1(self.conv1(x1)))
        v2 = self.maxpool(self.relu2(self.conv2(v1)))
        v3 = torch.cat([v1, v1, ... , v1], 0)  # Concatenation of the result tensor along a specified dimension
        return self.conv3(v2)


# Initializing the model
m = Model()


