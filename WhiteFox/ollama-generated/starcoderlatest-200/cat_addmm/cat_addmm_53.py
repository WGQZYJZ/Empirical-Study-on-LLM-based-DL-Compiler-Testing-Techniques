
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size, channel=8):
        super().__init__()
        self.fc = torch.nn.Linear(input_size, channel)
        self.conv = torch.nn.Conv2d(channel, 16, kernel_size=1)

    def forward(self, x1):
        v1 = F.relu(self.fc(x1))
        v2 = self.conv(v1)
        v3 = torch.addmm(v2, v2.T, v2)
        return v3
# Initializing the model
m = Model(input_size=1000, output_size=50)

# Inputs to the model
x1 = torch.randn(1, 1000)
