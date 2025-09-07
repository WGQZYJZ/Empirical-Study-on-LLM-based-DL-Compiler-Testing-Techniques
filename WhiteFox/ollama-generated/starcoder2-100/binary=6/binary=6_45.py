
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 9, 1)
 
    def forward(self, x1):
        v1 = F.max_pool2d(x1, 4, stride=2)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2) + 0.789 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 3, 576, 576)

## Input for max pooling and linear transformation
input_for_maxpooling = x1[:, :, -28:, :] # Slicing the input along channel (dimension 1), height (dimension 2) of the input to produce the input for the max pooling. 

## Input for convolutions in forward pass
input_for_conv = F.max_pool2d(x1, 4, stride=2) # Slicing the input along channel (dimension 1), height (dimension 2) of the input to produce the input for the convolutions.

## Input for convolution before linear transformation
input_for_lineartransformation = self.conv1(x1[:, :, -3:, :]) # Slicing the input along channel (dimension 1), width (dimension 0) and height (dimension 2) of the input to produce the input for the convolution in the forward pass, before linear transformation
