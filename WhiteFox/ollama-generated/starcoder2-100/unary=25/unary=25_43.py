
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.linear(x1)  # Apply a linear transformation to the input tensor
        v2 = (v1 > 0).float() * v1 + (-1 * v1).float()  # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise. Multiply the output of the linear transformation by -1 for the elements that are less than or equal to 0, and then choose the corresponding element from t2, which multiplies each element that is greater than 0 with itself. This essentially implements the Leaky ReLU activation function
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4) # Create a vector of random numbers as an input tensor for the model. The vector should be of shape (batch_size, size...)
__output__  = m(x1)

