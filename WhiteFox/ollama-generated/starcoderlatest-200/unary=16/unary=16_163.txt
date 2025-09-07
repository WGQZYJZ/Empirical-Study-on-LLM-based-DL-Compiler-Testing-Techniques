
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*64, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # Flatten the input tensor with size (batch_size, 3, 64, 64) to a 1-D vector of size (32*64).
        v2 = torch.nn.functional.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
