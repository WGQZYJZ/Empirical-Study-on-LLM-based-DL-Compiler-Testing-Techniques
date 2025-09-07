
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)

        # Change this line:
        v2 = 5 * v1  # Multiply the output of the convolution by a constant 5
        __v3__ = torch.nn.functional.relu(v2 - other_tensor)  # Apply the ReLU (Rectified Linear Unit) activation function to the result

        return __v3__


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other_tensor  = torch.randn(8, 8) + 5

