
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other # Add another tensor to the output of the linear transformation
        v2 = torch.relu(v1) # Apply the ReLU activation function to the result
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 8) # other tensor should be a valid input for self.linear(x1) + other
