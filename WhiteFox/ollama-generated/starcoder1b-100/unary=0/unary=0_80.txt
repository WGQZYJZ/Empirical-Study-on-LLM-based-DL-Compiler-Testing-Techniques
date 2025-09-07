
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = (v1  # Square
         .view(-1, 1, -1, -1)  # Expand each of the four output features to a single channel dimension
         .expand_as(v1)  # Make sure that the shape is compatible with a convolution operation
         ) * v1  # Cube
        v3 = (v2  # Multiply each of the output channels by itself
         .view(-1, 1, -1, -1)  # Expand each of the four input features to a single channel dimension
         .expand_as(v2)  # Make sure that the shape is compatible with a convolution operation
         )
        v4 = torch.tanh((v3 * (0.044715 )).view(-1, 1))  # Apply the hyperbolic tangent function to each of the input channels
        return v4 + 1


# Initializing the model
m = Model()


