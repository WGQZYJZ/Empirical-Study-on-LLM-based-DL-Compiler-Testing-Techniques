
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 7 * 7, 1000)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 256 * 7 * 7)) # Apply a linear transformation to the input tensor with size (batch_size * N, input_size)
        v2 = torch.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
