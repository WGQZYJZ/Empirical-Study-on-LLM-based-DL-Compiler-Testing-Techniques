
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v1  = self.linear(x) # Apply the linear transformation to the input tensor 
        v2 = self.relu(v1)# Apply the ReLU activation function to the output of the linear transformation   
        return v2

# Initializing the model
m  = Model()


# Inputs to the model:
x1 = torch.randn(3, 32) # Assuming this is an input tensor for the model.

__output__  = m(x1)


