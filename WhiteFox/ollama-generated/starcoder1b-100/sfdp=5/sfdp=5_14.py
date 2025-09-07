
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 1)
        self.pool   = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2 = torch.nn.Conv2d(64, 128, 1)
        self.pool2 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        self.fc = torch.nn.Linear(128 * 4 * 4, 500)

        self.dropout = torch.nn.Dropout(0.3)

    def forward(self, x):
        # First convolution layer: input_tensor = [batch size, channel number, height, width]
        # MaxPool2D output shape: [batch size, channel number, height / 2, width / 2]
        x = self.pool(F.relu(self.conv1(x)))

        # Second convolution layer: input_tensor = [batch size, channel number, height / 2, width / 2]
        # MaxPool2D output shape: [batch size, channel number, height / 4, width / 4]
        x = self.pool2(F.relu(self.conv2(x)))

        # Fully connected layer: input_tensor = [batch size, channel number * height / 4 * width / 4]
        # Linear output shape: [batch size, channel number * height / 4 * width / 4]
        x = self.dropout(torch.relu(self.fc(x)))

        return x

# Initializing the model
m = Model()


