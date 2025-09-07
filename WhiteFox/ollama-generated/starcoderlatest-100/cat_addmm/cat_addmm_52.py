
class Model(torch.nn.Module):
    def __init__(self, num_channel=3, num_fc_layer=1, dropout_rate=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_channel, 8, 1)

        # Adding a fully connected layer
        fc_layer = []
        for i in range(num_fc_layer):
            fc_layer.append(torch.nn.Linear(64*7*7, 64))
        self.fc_layer = torch.nn.Sequential(*fc_layer)

        # Adding the dropout layer after the fully connected layer
        self.dropout = torch.nn.Dropout(dropout_rate)

    def forward(self, x):
        v1 = self.conv(x)  # Apply a convolution operation to the input tensor
        # Concatenate the results of each convolution into one large tensor and multiply it by the output of another convolution
        x_fc = torch.cat([v1 for i in range(3)], dim=1)
        v2 = self.fc_layer(x_fc).view(-1, 64*7*7)  # Apply a fully connected layer to the result tensor and reshape it as a 2D tensor
        v3 = torch.nn.functional.relu(v2)  # ReLU function on the output of the first convolution and apply dropout between layers
        return self.dropout(v3)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
