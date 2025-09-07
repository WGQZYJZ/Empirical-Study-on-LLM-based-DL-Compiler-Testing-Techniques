
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        v3 = torch.relu(v2)  # Apply the ReLU activation function to the result
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(8, requires_grad=True)  # Generate another tensor for testing
