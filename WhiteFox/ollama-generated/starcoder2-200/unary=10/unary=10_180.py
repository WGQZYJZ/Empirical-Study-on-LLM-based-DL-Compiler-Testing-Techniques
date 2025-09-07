
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 5)
 
    def forward(self, x1): 
        v1 = self.lin(x1) # Applying linear transformation to the input tensor
        v2 = v1 + 3   # Addition operation on the output of applying a linear transformation
        v3 = torch.clamp_min(v2, 0)  # Clamp function is used for clamping the output to a minimum of 0
        v4 = torch.clamp_max(v3, 6) # Clamp max is used here for clamping the output of the addition operation to a maximum of 6
        v5 = v4 / 6   # Divide by 6 function on the output of clamped operation
        return v5

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(20, 3, 8) # Generating random input tensors for each dimension and each channel. 
