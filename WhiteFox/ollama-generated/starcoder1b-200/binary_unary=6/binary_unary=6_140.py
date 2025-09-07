
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 0.5 # Subtraction of constant 0.5 from the output of linear transformation
        v2 = torch.relu(v1) # Apply ReLU activation function to the result
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
