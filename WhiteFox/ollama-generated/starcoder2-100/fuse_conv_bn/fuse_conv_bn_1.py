
class Model(torch.nn.Module):
    def __init__(self, conv_channels):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 40 * conv_channels[0], kernel_size=3)
        self.conv2 = torch.nn.Conv2d(40 * conv_channels[0] + 40 * conv_channels[1],
                                     40 * conv_channels[1],
                                     kernel_size=3,
                                     stride=2)

        self.relu = torch.nn.ReLU()
        self.linear = torch.nn.Linear(5760, 900)

    def forward(self, x):
        output = self.conv1(x)
        output = self.relu(output)
        output = self.conv2(output)
        output = self.relu(output)

        flattened_output = torch.nn.functional.flatten(output, start_dim=1)

        output = self.linear(flattened_output)

        return output


# Initializing the model
m  = Model([40])

