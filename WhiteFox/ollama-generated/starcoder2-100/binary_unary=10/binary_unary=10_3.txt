
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y):
        v1 = torch.nn.Linear()(x1) # Apply a linear transformation to the input tensor `x`
        v2 = v1 + y # Add another tensor to the output of the linear transformation 
        v3  = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing the model