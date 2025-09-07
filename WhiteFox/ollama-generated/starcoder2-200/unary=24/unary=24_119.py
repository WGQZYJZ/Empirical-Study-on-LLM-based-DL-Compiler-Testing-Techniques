
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)

        v2 = (v1 > 0).float() * 0.5 
        # Apply pointwise convolution with kernel size 1 to the input tensor
        # Multiply by negative_slope
        # Create a boolean mask where each element is True if it's greater than or equal to zero, and False otherwise
        # Select elements from v1 based on the mask
        v3 = torch.where(v2 == True , v1 * 0.5 + (torch.nn.init.calculate_gain("leaky_relu", negative_slope=negative_slope) * v1), v1 * 0.7071067811865476 )
        # Multiply by negative slope 
        # Apply the where function to select elements from t1 or t3 based on the mask
        return v3

# Initializing the model with negative_slope = -0.1 
m = Model(negative_slope=-0.1)

# Inputs to the model:
x1 = torch.randn(1, 3, 64, 64)

