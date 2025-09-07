
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1, dtype=torch.float) # Replace torch.rand_like with lowmem_dropout in the graph
        v3  = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias) 
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 5, 8) # Generate an input tensor of size [N x M] with random numbers

