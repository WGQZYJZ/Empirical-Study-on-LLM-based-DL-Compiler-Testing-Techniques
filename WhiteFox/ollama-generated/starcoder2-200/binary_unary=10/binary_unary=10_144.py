
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other_tensor # Add another tensor to the output of the linear transformation
        v3 = torch.relu(v2)  # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()
 

# Inputs to the model
x = torch.randn(10, 1024)
__output__  = m(x)

