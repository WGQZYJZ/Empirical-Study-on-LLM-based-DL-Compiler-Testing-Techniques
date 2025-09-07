
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1  = self._linear(x1)
        v2  = v1 + torch.randn(320) if other is None else v1 
        v3  = torch.relu(v2)
        return v3
   
class ReLULayer(torch.nn.Module):
 
    def __init__(self, num_channels):
        super().__init__()
        self._num_channels  = num_channels 
        self._conv  = torch.nn.Conv2d(in_channels=1, out_channels=self._num_channels, kernel_size=(3, 3), padding=1)
        self._batchnorm  = torch.nn.BatchNorm2d(self._num_channels)
 
    def forward(self):
        return torch.relu(self._conv(x))


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(320, 8, 576 // 8)
 
# Apply ReLU
output_tensor  = m(x1)
 
