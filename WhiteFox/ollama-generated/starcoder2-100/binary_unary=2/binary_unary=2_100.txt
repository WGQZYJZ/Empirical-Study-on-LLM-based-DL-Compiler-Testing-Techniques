
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 - other  # Subtract a tensor or scalar "other" from the output of the convolution 
        return torch.relu(v2)


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 64, 800, 500)
other  = torch.randn(3, 128, 97, 100) # This is an "other" tensor with random values that are used to test the model. This tensor may have come from anywhere and have been passed as input during training. However, it should not be used in the actual model.
