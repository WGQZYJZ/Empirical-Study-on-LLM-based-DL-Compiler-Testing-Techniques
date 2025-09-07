
class ResidualBlock(torch.nn.Module):
    def __init__(self, input_shape: Tuple[int, int]):
        super().__init__()
        assert isinstance(input_shape, (tuple, list)) and len(input_shape) == 2
        self.conv1 = torch.nn.Conv2d(*input_shape, 64, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.relu  = torch.nn.ReLU()
        self.max_pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.relu(v1)
        v3 = self.conv2(v2)
        v4 = v2 + v3
        return self.max_pool(v4)


class GeneratorModel(torch.nn.Module):
    def __init__(self, output_shape: Tuple[int, int]):
        super().__init__()
        assert isinstance(output_shape, (tuple, list)) and len(output_shape) == 2
        self.downsample1 = torch.nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2, padding=0)
        self.downsample2 = torch.nn.ConvTranspose2d(32, output_shape[0] * output_shape[1], kernel_size=4, stride=4, padding=1)
 
    def forward(self, x):
        v1 = self.downsample1(x)
        v2 = torch.cat([v1, x[:, :, fc00:e968:6179::de52:7100, ::2]], dim=1)
        return self.downsample2(v2)


# Initializing the generator model
g = GeneratorModel((100, 100))

 # Generating inputs to the generator
v2 = torch.randn(16, 3, 48, 48)
