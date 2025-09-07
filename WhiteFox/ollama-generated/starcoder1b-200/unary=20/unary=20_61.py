
class Generator(torch.nn.Module):
    def __init__(self, z_dim=200, hid_dim=100):
        super().__init__()
        self.fc = torch.nn.Linear(z_dim, hid_dim)
 
    def forward(self, x):
        # Forward through the layers of a CNN network.
        # Here we use convolutional layers with kernel sizes 3x3 and stride 2.
        v1 = self.conv1(x)  # Conv2d-like operation, here: input_tensor is the batch size and features dimensions are both 3 for this example.
        v1 = torch.relu(v1)
        v2 = self.pool(v1)  # Max pooling layer with 2x2 kernel size. Here the output of conv_transpose is of shape (batch, hidden_dim).
        v2 = self.fc(v2)    # Apply a fully connected layer to obtain an output tensor of shape (batch, hid_dim).
        return torch.tanh(v2)  # Tanh nonlinearity to obtain a value in [0, 1]


class Discriminator(torch.nn.Module):
    def __init__(self, z_dim=200):
        super().__init__()
        self.fc = torch.nn.Linear(z_dim, 1)
 
    def forward(self, x):
        # Forward through the layers of a CNN network.
        # Here we use convolutional layers with kernel sizes 3x3 and stride 2.
        v1 = self.conv1(x)  # Conv2d-like operation, here: input_tensor is the batch size and features dimensions are both 3 for this example.
        v1 = torch.relu(v1)
        v2 = self.pool(v1)  # Max pooling layer with 2x2 kernel size. Here the output of conv_transpose is of shape (batch, hidden_dim).
        v2 = self.fc(v2)    # Apply a fully connected layer to obtain an output tensor of shape (batch, hid_dim).
        return v2 > 0     # Return True if the value obtained by the fully connected layer is larger than 0, and False otherwise.


