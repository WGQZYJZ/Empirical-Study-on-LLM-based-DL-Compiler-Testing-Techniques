
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1.permute(0, 2, 1), ...) # Permute the input tensor, swap last two dimensions and call linear function on it
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5) # create the first 5 elements of a new 1D tensor with standard normal distribution
__output__  = m(x1)