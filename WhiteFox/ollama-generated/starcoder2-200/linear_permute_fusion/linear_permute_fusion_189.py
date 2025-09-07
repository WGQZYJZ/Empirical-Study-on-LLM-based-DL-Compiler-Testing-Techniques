
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v3 = torch.nn.functional.linear(x1) # Apply linear transformation to the input tensor.
        v4  = torch.transpose_(v3, -2,-1)# Permute the output tensor from the linear transformation.

        return v4

# Initializing the model