
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        v3 = relu(v2)     # Apply the ReLU activation function to the result
        return v3


# Inputs to the model
x1 = torch.randn(1, 8)
other = torch.tensor([1., -0.5], dtype=torch.float64)
