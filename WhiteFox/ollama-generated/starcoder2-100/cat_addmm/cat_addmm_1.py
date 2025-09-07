
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.cat([v2], dim) # Concatenate the result along a specified dimension (dimension should be less than the dimensionality of input tensor in this example: 0)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 27, 96)
mat1 = torch.randn(8, 96, 45) # Dimensions: batch size (8), output channels of first linear layer (96 in this example) and input channel of first convolutional layer (in the example 3). These dimensions are fixed for this model. 
mat2 = torch.randn(8, 100, 34) # Dimensions: batch size (8), output channels of second linear layer (100 in this example) and input channel of first convolutional layer (in the example 3). These dimensions are fixed for this model.
