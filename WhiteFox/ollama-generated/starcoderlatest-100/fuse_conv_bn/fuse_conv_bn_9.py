
class Model(torch.nn.Module):
    def __init__(self, kernel_size=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # Convolution layer in module api.

    def forward(self, x):
        conv = self.conv(x)    # Apply convolution layer to the input tensor.
        bn   = torch.nn.functional.batch_norm(conv) # Apply batch normalization on the output of the convolution layer.
        return bn
        
# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 2, 20, 40)
