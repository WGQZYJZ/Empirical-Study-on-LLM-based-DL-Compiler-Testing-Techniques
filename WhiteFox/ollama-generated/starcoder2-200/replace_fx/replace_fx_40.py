
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.nn.functional.dropout(x1, p=0) # Apply dropout to the input tensor (replace)
        v4  = torch.rand_like(v3, requires_grad=True) # Generate a tensor with the same size as input_tensor filled with random numbers (replace)
        v5  = x1 + v4 + v2 # The inputs to the add operation will not be erased because they are not replaced by a new input.

        return [v3, v4]

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5)