
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.2)
        v2 = torch.rand_like(v1) # Generate a random tensor with the same size as input_tensor filled with random numbers

        return (v1, v2)

# Initializing model
m = Model()
# Inputs to the model
x1 = torch.randn(3, 4)

# Running inference using initial inputs x1 and checking that the output is correct.
