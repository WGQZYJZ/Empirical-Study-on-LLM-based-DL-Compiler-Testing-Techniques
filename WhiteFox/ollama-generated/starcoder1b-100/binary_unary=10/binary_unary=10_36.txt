
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1 = x1.view(x1.shape[0], -1)  # Flatten the input tensor (t1 is 28 x 28).
        v2 = self.linear(v1)  # Apply a linear transformation to t1.
        v3 = torch.relu(v2)  # Apply the ReLU activation function to t2.
        return v3


# Inputs to the model
x1 = torch.randn(4, 784)
