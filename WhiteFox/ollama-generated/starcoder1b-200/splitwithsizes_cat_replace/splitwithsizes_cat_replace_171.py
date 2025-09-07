
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Forward pass function
        output = torch.split(x1, [64, 32, 8], dim=0)   # Split the input tensor into several tensors along a given dimension
        return self.conv_stack(output)     # Stack multiple split tensors for more efficient batch-wise convolution


# Initializing the model
m = Model()


