
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)

    def forward(self, x1):
        bn = torch.nn.functional.batch_norm(...)  # Batch normalization layer using functional API
        conv = torch.nn.functional.conv2d(...)  # Convolution layer using functional API
        return bn(x1)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
