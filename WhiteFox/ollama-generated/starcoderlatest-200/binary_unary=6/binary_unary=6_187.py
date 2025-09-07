
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # The shape of the input tensor should be N * C * H * W, where N is batch size, C is number of channels, and H is height and W is width
        v2 = v1 - 1 # Subtract 1 from the output of the linear transformation
        v3 = torch.nn.functional.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28*28)
