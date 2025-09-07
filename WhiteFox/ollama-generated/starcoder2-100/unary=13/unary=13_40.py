
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1) # Applying pointwise convolution with kernel size 1 to the input tensor
        self.linear  = torch.nn.Linear(in_features=64*64*8, out_features=64*64*8) # Apply a linear transformation with 3072 (input dimensions) as the number of features in each dimension
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = self.conv(x1)  # Applying pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * t1 # Multiply the output of the pointwise convolution by a constant
        v3  = v1 * 0.7071067811865476 # Apply a sigmoid function to the output of the pointwise convolution, multiplying each of its channels by another constant value
        v4  = self.sigmoid(v2) 
        v5  = v3 + t2  # Add `t2` to the output of the sigmoid function
        v6  = v1 * 0.7071067811865476 # Apply a pointwise convolution with kernel size 1 on top of the output of the pointwise convolution
        return v3


# Initializing model
m  = Model()

# Inputs to the model:
x1  = torch.randn(2, 3, 64, 64)
__output__  = m(x1)
