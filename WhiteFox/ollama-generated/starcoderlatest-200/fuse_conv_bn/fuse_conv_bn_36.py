
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, kernel_size=3)

    def forward(self, x):
        output = torch.nn.functional.conv2d(x, weight=self.conv.weight, bias=self.conv.bias, stride=(1, 1), padding=(0, 0)) # Functional API pattern
        return output

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 3, 32, 32)
