
class Model(torch.nn.Module):
    def __init__(self, channels, num_filters, hidden_layer_num):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(channels, num_filters, 3, stride=1, padding=1)

        self.linear_layers = [
            # Input shape is (batch, channels, kernel_size, input_width // kernel_size)
            torch.nn.Linear(num_filters * (2 * hidden_layer_num + 1), num_filters),
        ]

        for i in range(hidden_layer_num):
            self.linear_layers.append(
                torch.nn.ReLU(inplace=True))

        self.conv2 = torch.nn.Conv2d(num_filters, channels, 3, stride=1, padding=1)

    def forward(self, x):
        # Use the input as is to get the feature map from conv1
        v0 = self.conv1(x)

        for linear in self.linear_layers:
            v0 = linear(v0)
        
        # Perform matrix multiplication on the feature map from conv1 and get it from conv2
        v1 = torch.cat([torch.mm(v0, m), torch.ones(v0.size())], dim=1)
        v2 = self.conv2(v1)

        return v2


# Initializing the model
m = Model(3, 64, hidden_layer_num=1)
