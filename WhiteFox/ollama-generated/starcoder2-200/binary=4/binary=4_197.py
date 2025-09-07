
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, weight=None) # Apply a linear transformation to the input tensor with a randomly generated matrix as weights
        v2  = v1 + other # Add another randomly generated tensor to the output of the linear transformation
        return v2


# Initializing the model