
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(64, 784)
__output__  = m(x1)

# A possible example: Generate an input tensor with 5000 entries in the first dimension and 350 x 220 pixel values each. Apply a linear transformation to this tensor using torch.nn.Linear(). Pass this output through a sigmoid function using torch.sigmoid(). Then, pass the output of the sigmoid function as input into another torch.nn.Linear() module.

# Initializing a random tensor x1 with 5000 entries in the first dimension and 350 x 220 pixel values each. Applying a linear transformation to this tensor using torch.nn.Linear(). Passing that output through a sigmoid function using torch.sigmoid() results in a new tensor with 14896 entries of which half is zero. This new tensor represents the input data for another torch.nn.Linear() module. Passing it through this torch.nn.Linear() module is similar to gating mechanisms, where we control the flow of information by applying sigmoid functions and multiplying their outputs.

# A possible example: Generate a 64 x 350 x 220 tensor. Apply a pointwise convolution with kernel size 1 on this tensor using torch.nn.Conv2d(). Add 0 to the output of the convolution, resulting in another 64 x 350 x 220 tensor that represents input data for a linear transformation. Then, pass the output of the convolution operation through another torch.nn.Linear() module.

# Initializing random tensors x1 and x2 with shapes (64, 350, 220) each. Applying a pointwise convolution to these tensors using torch.nn.Conv2d(). The resulting tensor is of shape (19, 8, 7). Pass this output through a linear transformation using torch.nn.Linear() and pass the result as input to another torch.nn.Linear() module. The first linear transformation passes an output with 350 x 24 values each while the second linear transformation is passing an output of 19 x 8 = 152 elements. 

# A possible example: Generate a random tensor x with shape (64, 784). Apply a pointwise convolution to this tensor using torch.nn.Conv2d(). Passing the output of that operation as input into another torch.nn.Linear() module results in an output of size (19, 350) = 6510. Passing these 6510 elements through a sigmoid function using torch.sigmoid(), we obtain a new tensor of shape (64, 784). Passing this new tensor as input to another torch.nn.Linear() module results in an output with 392 elements that represents input data for another gating mechanism by applying the sigmoid function and multiplying it by the output from previous linear transformation.
