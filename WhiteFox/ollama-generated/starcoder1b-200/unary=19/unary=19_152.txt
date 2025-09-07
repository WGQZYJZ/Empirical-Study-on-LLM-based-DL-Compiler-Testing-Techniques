
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1 = x1.view(-1, 28 * 28)  # Convert input tensor from N*784 to N*28*28
        v2 = self.linear(v1)  # Apply the linear transformation
        return torch.sigmoid(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 784)  # Input tensor with shape (N, D)
