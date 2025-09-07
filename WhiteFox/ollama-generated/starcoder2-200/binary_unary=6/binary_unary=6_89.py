
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, oth):
        v1 = torch.nn.functional.linear(x1)  # Apply a linear transformation to the input tensor
        v2 = v1 - oth                        # Subtract 'other' from the output of the linear transformation
        v3 = torch.relu(v2)                  # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 50)
oth = torch.randn(50,)
__output__  = m(x1, oth)

