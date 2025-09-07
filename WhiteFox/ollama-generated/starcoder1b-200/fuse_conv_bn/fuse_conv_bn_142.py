
class ConvModel(torch.nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = torch.nn.Conv1d(channels, 20, kernel_size=3)
        self.batch_norm1 = torch.nn.BatchNorm1d(20)
        self.conv2 = torch.nn.Conv1d(20, 40, kernel_size=3)
        self.batch_norm2 = torch.nn.BatchNorm1d(40)

    def forward(self, x):
        v1  = x.permute(0, 2, 1)
        v2  = self.conv1(v1)
        v3  = self.batch_norm1(v2)
        v4  = torch.nn.functional.relu(v3)
        v5  = self.conv2(v4)
        v6  = self.batch_norm2(v5)
        v7  = torch.nn.functional.relu(v6)
        return v7


# Initializing the model
m = ConvModel(channels=3)


# Inputs to the model
x1 = torch.randn(1, 40, 20)
