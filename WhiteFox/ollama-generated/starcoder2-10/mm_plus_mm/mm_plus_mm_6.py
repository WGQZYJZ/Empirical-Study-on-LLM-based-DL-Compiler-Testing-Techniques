
class Model(torch.nn.Module):
    def __init__(self, a):
        super().__init__()
        self.a  = torch.nn.Parameter(
            torch.tensor([1]),
            requires_grad=True)
 
    def forward(self, x1):
        v1  = torch.mm(x1, x2) # Matrix multiplication between the input and input2 
        v4  = torch.matmul(v3, x5) # Multiplication of the first matrix product with input6
        return self.a * (v4 + v1) # Multiplying the result by a constant, and then multiplying that constant by the output from the matrix multiplication
 

# Initializing the model and setting its initial parameters. 
m = Model()


# Inputs to the model
x1 = torch.randn(320, 480) # Input for the multiplication with input2 (x2). The size of this tensor can be specified by the user as long as it is not smaller than the size that would result from a pointwise convolution, or a matrix multiplication.
input_tensor = torch.randn(320, 150) # Input for the matrix multiplication with input6 (x5). The size of this tensor can be specified by the user. 
m(x1)

