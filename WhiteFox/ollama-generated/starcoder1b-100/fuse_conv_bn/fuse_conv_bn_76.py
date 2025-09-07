
class FusionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Use the model_input as input to a convolution layer and batch normalization layer.
        conv  = torch.nn.functional.conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        bn  = torch.nn.functional.batch_norm(...)
        output  = bn(conv(model_input))
        return output

# Initializing the model
m = FusionModel()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
