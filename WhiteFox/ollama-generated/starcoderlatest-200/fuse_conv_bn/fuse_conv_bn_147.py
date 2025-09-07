
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # Convolution layer
        self.bn = torch.nn.BatchNorm2d(...)   # Batch Normalization layer

    def forward(self, x1):
        output = F.batch_norm(...)
        conv_output = self.conv(...).relu()
        return output + conv_output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 56, 56)
