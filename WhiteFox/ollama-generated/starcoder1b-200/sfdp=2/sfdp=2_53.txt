
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.fc = torch.nn.Linear(8 * 64 * 64, 8)
 
    def forward(self, x):
        # x: (batch_size, channels, width, height)
        batch_size, channels, width, height = x.shape
        x = F.adaptive_avg_pool2d(x, output_size=(1, 1))  # Average the pixels over spatial dimensions.
        # x: (batch_size, channels * width * height)
        x = x.reshape(batch_size, -1)
        x = self.conv1(x).reshape(batch_size, channels, width, height)
        x = x.view(batch_size, channels, -1)
        x = F.relu(self.fc(x))
        return x


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 3, 64, 64)
