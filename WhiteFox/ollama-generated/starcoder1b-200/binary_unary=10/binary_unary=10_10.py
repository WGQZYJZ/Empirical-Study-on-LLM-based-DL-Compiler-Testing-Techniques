
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Apply a linear transformation to the input tensor
        v2 = relu(v1)  # Apply the ReLU activation function to the result
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4096)
