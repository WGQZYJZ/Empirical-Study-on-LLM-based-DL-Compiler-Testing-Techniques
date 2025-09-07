
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = torch.rand_like(x1, dtype=torch.float32) # Generate a tensor with the same size as input_tensor filled with random numbers
        v1  = torch.nn.functional.dropout(v0, p=0.5, inplace=True)
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply dropout to the input tensor. The random numbers of `x1` will be replaced by zeros with probability 50%.
        return v2

# Initializing the model
m  = Model()

