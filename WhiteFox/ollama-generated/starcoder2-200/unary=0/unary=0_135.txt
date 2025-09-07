
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5 # Apply the multiplication
        v3  = v1 * v1  # Apply the square operation to the output of the convolution
        v4  = v1 + v3  # Add the result of the square operation to the convolution's output
        v5  = torch.sqrt(v4) 
        v6  = v2 / v5 # Divide the first operation by the rooted of the result of the previous operation (this is just another way of implementing sqrt)
 
        v7  = v3 * 0.12952180519034
        v8  = torch.log(v6 + v7 ) # Apply the logarithm to the first operation, and then add a constant to the output of the previous operation
        v9  = tanh(v8) 
        v10  = v2 * v9 
        return v10


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1,3,64,64)
