
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64 * 7 * 7, 10)
 
    def forward(self, x):
        v = self.conv(x)  # Apply pointwise convolution with kernel size 1 to the input tensor
        negative_slope = torch.randn(v.shape[1], device=device)  # Create a random number in [-3, -5]
        v2 = torch.where(torch.abs(v).gt(0), v, v * negative_slope)  # If the corresponding element of `v` is greater than or equal to zero, set it to its value, otherwise set it to its output multiplied by the negative slope
        return self.linear(v2)  # The output of the linear transformation is now taken as input to the ReLU activation function


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
