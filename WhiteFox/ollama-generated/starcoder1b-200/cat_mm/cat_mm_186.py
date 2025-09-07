
class Model(nn.Module):
    def __init__(self, input1_channels=200, input2_channels=30):
        super().__init__()
        self.input1_conv = nn.Conv2d(input1_channels, input2_channels // 2, kernel_size=3, stride=1, padding=1)
        self.input2_conv = nn.Conv2d(input2_channels // 2, input2_channels * 2, kernel_size=5, stride=2, padding=2)
        self.fc = torch.nn.Linear(200 * 32 * 32, 1)
 
    def forward(self, x1):
        v1 = F.relu(self.input1_conv(x1))
        v2 = self.input2_conv(v1)
        v3 = torch.cat([v1, v2], dim=1)
        return self.fc(v3)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 10, 64, 64)
