
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv_transpose(x1)
        v2  = F.sigmoid(v1) 
        v3  = v1 * v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


__output__  = m(x1)

# Please provide a sample of code (in C, Python or Java programming language) that will generate 2 random tensors:
## 1st input tensor: a 3D Tensor with shape [N, 3, 7] of type torch.float. 
## 2nd output tensor: a vector of size N. The content should be generated using random values and uniform distribution.

50% of the probability that the result should be 1 (that is, value that lies in the interval [-1, 1]), otherwise 50% of the probability will be -1.


# Description of requirements
- In the beginning of the program, you are required to call the `torch.rand` function from `torch.distributions`, with size [N, 3]. This function will generate a random tensor of shape `[N, 3]` with values in interval `[0, 1)`. You have to pass two more arguments: mean and std. Use `mean=0` (the default value) for the mean argument; use standard deviation `std = 1` for it too.
- For a 2D tensor you can set the shape equal to [N] x 3. In this case, 50% of the probability will be 1 and the other half - is -1 (because this is uniform distribution with mean value 0).
- The number `N` is fixed but it could change depending on your settings in the `torch.rand` function.

