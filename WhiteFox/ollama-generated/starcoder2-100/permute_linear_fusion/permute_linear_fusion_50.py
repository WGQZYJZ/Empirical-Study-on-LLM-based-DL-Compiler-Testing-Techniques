
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randperm(x1) # Randomly permute an input tensor.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(400)
__output__  = m(x1)


