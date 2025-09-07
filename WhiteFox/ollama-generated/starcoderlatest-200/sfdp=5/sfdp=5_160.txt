
class Model(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(input_dim, 32, kernel_size=8),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=4) # The stride of the maxpool layer is set to 4
        )

    def forward(self, x1):
        v1 = self.layer1(x1)
        return v1

# Initializing the model
m = Model(3)

# Inputs to the model
x1 = torch.randn(1, 256, 80, 80)
