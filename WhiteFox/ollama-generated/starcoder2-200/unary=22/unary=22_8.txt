
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Initialize the model class with a forward() method that accepts an input tensor and returns the output of the linear transformation plus tanh activation function.
        v1 = torch.linear(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model