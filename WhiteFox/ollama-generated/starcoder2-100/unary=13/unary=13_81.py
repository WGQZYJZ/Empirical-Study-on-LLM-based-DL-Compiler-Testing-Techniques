
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 1)

    def forward(self, x): 
        v1  = self.linear(x.reshape(-1)) # Apply a linear transformation to the input tensor, reshaping it into a vector of size 289
        v2  = torch.sigmoid(v1)# Apply the sigmoid function to the output of the linear transformation
        v3  = v1 * v2 # Multiply the output of the linear transformation by the output of the sigmoid function
        return v3


# Initializing the model and assigning it to a new variable `m`.
m = Model()

# Inputs to the model. The tensor is reshaped into a 64-by-64 image, which will be fed as input to m.reshape(-1). Then, the linear transformation takes the input and applies a dot product to the output vector of size 289 using parameters.
x = torch.randn(3, 64 * 64)  # Recall that the input tensor is flattened before being passed through the model.
