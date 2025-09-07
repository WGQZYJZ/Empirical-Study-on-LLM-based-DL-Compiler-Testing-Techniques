
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, 5) # Replace 'conv' with other layer name if necessary
        self.batch_norm = torch.nn.BatchNorm2d(32)

    def forward(self, x):
        conv_result = self.conv(x)
        output = self.batch_norm(conv_result)
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 28, 28) # Replace '1', '32' and '5' with correct values based on input tensor shape.
