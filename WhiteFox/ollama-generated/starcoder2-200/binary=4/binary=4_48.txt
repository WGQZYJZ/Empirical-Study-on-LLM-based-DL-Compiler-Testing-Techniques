
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3 = v1 * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
        v4 = torch.erf(v3) # Apply the error function to the output of the convolution
        v5 = v4 + 1 # Add 1 to the output of the error function
        v6 = v2 * v5 # Multiply the output of the convolution by the output of the error function
        return v6, x1, v3


# Initializing model. We provide the second tensor that is added as input into the linear transformation
m  = Model()

# Input to the model (also the first tensor that is used in the linear transformation)
x1  = torch.randn(256, 3, 64, 64)

# Second tensor passed to the model as input to the linear layer
other_input  = torch.randn(256, 8, 3, 3)


# Initializing model (again with the second tensor as an input in the linear layer). We also pass another constant value for the input to the convolutional layer. This would be a good scenario to demonstrate that adding the second tensor as input to the convolution layer does not alter the output of the model, since no additional tensor  `other` is added to the output of this convolutional transformation
m2 = Model()

# Input for the second model
x12 = torch.randn(256, 3, 8)


# Inputs to the model (for both models with different input tensors). We add a constant value that is not part of either input tensor. This would be an excellent scenario to demonstrate that adding another tensor as input does not alter the output of the model. This addition has no effect on the output of the model since no additional tensor  `other`is added to the output of this linear transformation
__output__, _ = m(x1, other_input)

