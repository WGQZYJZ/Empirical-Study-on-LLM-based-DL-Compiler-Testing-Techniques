
class Model(torch.nn.Module):
    def __init__(self, inputsize=1000, outputsize=500):
        super().__init__()
        self.linear = torch.nn.Linear(inputsize, 2 * 36) # Apply a fully connected layer to the input tensor and add 2 * 36 bias terms

    def forward(self, x1):
        v1  = self.linear(x1) # Apply the linear transformation
        v2  = torch.nn.functional.dropout(v1, p=0.45) # Dropout layer for inputs to transformer layers (default dropout probability of 0.5)
        v3  = torch.nn.Functional.gelu(v2) + 0.7896  # Apply GELU activation function with 0.7896 bias
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3 * 45)
