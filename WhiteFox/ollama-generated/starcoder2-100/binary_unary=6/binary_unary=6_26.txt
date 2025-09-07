
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1)  # Apply linear transformation to input tensor
        
        # Subtract 2 from output of linear transformation
        v3  = torch.abs(v1 - 2) 
        v4  = torch.nn.functional.relu(v3) # ReLU activation function
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(6, 8)

# Output of the model on the input tensor x1
output_m  = m(x1)

