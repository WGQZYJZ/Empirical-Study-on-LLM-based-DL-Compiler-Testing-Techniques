
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + kwargs["other"] # Replace "kwargs" with the input dictionary
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Define another tensor for the addition operation
other_tensor = torch.randn(1, 8, 64, 64)

# Update the inputs dictionary with the keyword argument to add to the convolution output
inputs_dict  = {"other": other_tensor}

 # Calling the model and adding a third convolution block to the graph of operations
__output__  = m(x1)

