
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output = torch.nn.functional.batch_norm(torch.nn.functional.conv2d(x1))
        return output  # Use batch normalization in evaluation mode when the model is exported to TorchScript

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
