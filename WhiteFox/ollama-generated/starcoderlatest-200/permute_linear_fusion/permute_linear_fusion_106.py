
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3): # add some inputs here
        v1 = torch.tensor([x1, x2, x3]).permute(0, 2, 1) # permute the input tensor
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 4, 2)
x3 = torch.randn(1, 5, 2)
