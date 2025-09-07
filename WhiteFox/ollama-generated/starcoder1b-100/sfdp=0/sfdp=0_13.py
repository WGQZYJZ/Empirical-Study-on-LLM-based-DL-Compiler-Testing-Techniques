
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm(3)
        self.conv1 = nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = nn.Conv2d(8, 4, 1, stride=1, padding=0)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.layer_norm(x)
        x = F.dropout2d(self.relu(self.conv1(x)), p=0.5)
        x = F.dropout2d(F.adaptive_avg_pool2d(self.relu(self.conv2(x))), p=0.5)
        return x


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
