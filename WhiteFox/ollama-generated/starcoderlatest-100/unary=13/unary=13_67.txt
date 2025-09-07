
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 28*28)) # Flatten input tensor to (batch size, feature vector dimension) and apply linear transformation
        v2 = torch.sigmoid(v1) # Apply sigmoid function to the output of the linear transformation
        v3 = v1 * v2 # Multiply the output of the linear transformation by the output of the sigmoid function
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64) # Note that the size of input tensor must be (batch size, channel dimension, height, width) and we use the flattened version of the input tensor here for simplicity's sake
