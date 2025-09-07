
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other  # Add another tensor to the output of the linear transformation (if available)
        else:
            v2 = v1
        v3 = torch.nn.functional.relu(v2)  # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 1024)
other_tensor  = torch.rand(1, 512) # a randomly initialized tensor of shape [batch size x features]
__output__  = m(x1, other=other_tensor)
