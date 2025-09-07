
class Model(torch.nn.Module):
    def __init__(self, num_layers=3):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)

        self.fc1 = torch.nn.Linear(3200, 4096)
        self.fc2 = torch.nn.Linear(4096, 4096)

        for layer_idx in range(num_layers):
            self.layer_idx = layer_idx + 1
            # The last `Conv` and `Linear` layers are not included here
            if layer_idx < num_layers - 1:
                setattr(self, f'layer{layer_idx+1}', torch.nn.BatchNorm2d(16))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1  # v2 has the same data as v1
        v3 = v2  # v3 has the same data as v1
        v4 = self.conv2(v3)
        v5 = v4  # v5 has the same data as v1
        v6 = torch.cat([v5, x1], dim=1)  # Add the input tensor along a specified dimension to the output of conv2
        v7 = self.conv3(v6)
        v8 = v7  # v8 has the same data as v7

        v9 = v8  # v9 has the same data as v7
        v10 = torch.relu(self.fc1(v9))
        v11 = torch.relu(self.fc2(v10))
        return v11


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
