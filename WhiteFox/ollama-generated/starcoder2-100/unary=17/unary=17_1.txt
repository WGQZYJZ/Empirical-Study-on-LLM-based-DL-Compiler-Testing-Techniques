
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1)
        v2 = torch.nn.functional.relu(v1)  # Apply the ReLU activation function to the output of the transposed convolution 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
