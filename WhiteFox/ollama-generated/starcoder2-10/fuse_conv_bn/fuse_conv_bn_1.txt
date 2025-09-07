

class Model(torch.nn.Module):
    def __init__(self, conv_channels: int = 32):
        super().__init__()

        # Declare two convolutional layers with the given number of channels each.
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=conv_channels)
        self.conv2 = torch.nn.Conv2d(
            in_channels=conv_channels, out_channels=conv_channels // 2)

        # Declare a batch normalization layer with the same number of channels as the previous convolutional layer.
        self.batchnorm1 = torch.nn.BatchNorm2d(num_features=conv_channels)

    def forward(self, x):
        y = torch.nn.functional.relu(self.batchnorm1(
            self.conv1(x)))  # Apply relu function and batch normalization layer to the input tensor.
        return torch.nn.functional.relu(self.conv2(y))

# Inputs to model
input_tensor = torch.rand(size=(4, 3, 608, 750), dtype=torch.float) # 4 is the batch size.

# Initializing the model
m = Model()


# Inputs to the model
