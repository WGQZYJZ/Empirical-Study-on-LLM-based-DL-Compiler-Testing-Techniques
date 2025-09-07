
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = self.linear(x1)  # Apply a linear transformation to the input tensor
        v2 = v1 + other        # Add another tensor to the output of the linear transformation
        return v2

# Initializing the model