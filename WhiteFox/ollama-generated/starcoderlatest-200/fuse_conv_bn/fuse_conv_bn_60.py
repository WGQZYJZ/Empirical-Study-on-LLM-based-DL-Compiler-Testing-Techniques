
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3)

    def forward(self, x):
        return self.conv(x) # Output of the convolution layer is used as input to the batch normalization layer


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 32, 32)
