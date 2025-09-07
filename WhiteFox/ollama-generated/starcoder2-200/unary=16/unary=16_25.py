
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 10)

    def forward(self, x):
        v1 = self.linear(x) # Apply a linear transformation to the input tensor
        v2 = torch.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(64, 3072)
