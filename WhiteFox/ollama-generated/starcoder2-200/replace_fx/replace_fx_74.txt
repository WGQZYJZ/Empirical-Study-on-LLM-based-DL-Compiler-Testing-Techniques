
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor with probability 0.5.
        v2 = torch.rand_like(v1, dtype=torch.float32).requires_grad_() # Generate a tensor with the same size as input_tensor filled with random numbers and compute the gradients for it.
        return v1, v2

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4)


# Initializer
m(x1)

