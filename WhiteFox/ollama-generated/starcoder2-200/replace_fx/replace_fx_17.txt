
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor.
        v2  = torch.rand_like(v0, dtype=torch.float32) # Generate a tensor with the same size as input_tensor filled with random numbers.
        return v2

# Initializing model
m = Model()

# Inputs to the model
x1 = torch.randn(4896, 17058)
__output__  = m(x1)

