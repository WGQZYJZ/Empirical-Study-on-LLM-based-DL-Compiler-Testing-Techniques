
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1  = torch.nn.functional.linear(x1) # Applying a linear transformation to an input tensor
        v2  = v1 + other
        v3  = torch.nn.functional.relu(v2) # Applying the ReLU activation function on the output of applying a linear transformation to an input tensor, then another tensor is added to that output
        return v3

# Initializing the model