

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1, dtype=torch.float32) # Generate a tensor with the same size as input_tensor filled with random numbers
        v4  = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)

# Initializing the model