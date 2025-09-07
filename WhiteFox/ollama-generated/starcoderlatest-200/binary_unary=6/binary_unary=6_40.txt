
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # Flatten the input tensor and pass it to linear transformation
        v2 = v1 - 5 # Subtract 'other' from the output of the linear transformation
        v3 = torch.nn.ReLU()(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
