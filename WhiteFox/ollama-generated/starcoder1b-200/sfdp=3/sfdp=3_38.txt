
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, kernel_size=2, stride=1)
        self.conv = torch.nn.Conv1d(4, 6, kernel_size=3, stride=2, padding=0)
 
    def forward(self, x1):
        v1  = self.conv1d(x1)  # Apply a 1D convolution to the input tensor
        v2  = torch.nn.functional.pad(v1, (0, 1))  # Zero pad left and right of the convolution output to make it valid for attention mechanism
        v3  = self.conv(v2)  # Apply a 1D convolution to the zero padded output of the 1D convolution
        return torch.tanh(v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
