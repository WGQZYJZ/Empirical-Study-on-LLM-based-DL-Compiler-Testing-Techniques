
class Model(torch.nn.Module):
    def __init__(self, num_channels=32, conv_layer_dims=[16, 32], fc_layer_dim=8):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_channels, conv_layer_dims[0], kernel_size=3, stride=2, padding=1)
        self.pooling = torch.nn.MaxPool2d(kernel_size=3, stride=2)
 
        for _ in range(len(conv_layer_dims)-1):
            layer = torch.nn.Conv2d(conv_layer_dims[_], conv_layer_dims[1], kernel_size=3, stride=2, padding=1)
            setattr(self, f'layer{_+1}', layer)
 
        layer = torch.nn.Linear(4096, fc_layer_dim)
        setattr(self, 'fc', layer)
 
    def forward(self, x):
        v1 = self.conv(x)  # Apply a convolutional operation to the input tensor.
        v2 = self.pooling(v1)  # Apply max pooling operation with kernel size (3, 3).
 
        for _ in range(len(conv_layer_dims)-1):
            if hasattr(self, f'layer{_+1}'):
                v3 = getattr(self, f'layer{_+1}')(v2)  # Apply a convolutional operation to the output of max pooling.
                setattr(self, f'layer{_+1}_activated', torch.nn.ReLU()(v3))  # ReLU activation function on layer outputs.
            else:
                raise AttributeError('layer does not exist.')
 
        v4 = getattr(self, f'fc')(getattr(self, 'layer5_activated'))
        v5 = torch.cat([v1, v2] + [getattr(self, f'layer{_+1}_activated') for _ in range(len(conv_layer_dims)-1)], dim=1)
        v6 = getattr(self, 'fc')(v5)
 
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 32, 8, 40)
 
 # Outputs of the model
