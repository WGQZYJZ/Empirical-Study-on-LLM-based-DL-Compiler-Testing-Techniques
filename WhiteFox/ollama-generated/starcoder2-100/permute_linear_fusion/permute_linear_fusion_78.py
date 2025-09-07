
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1   = x1.permute(0, 2, 1) # Permute the input tensor to make the last two dimensions the first and second.
        v2_1 = self.linear(v1)     # Apply linear transformation to permuted tensor.
        v3  = torch.nn.functional.linear(v1, ...)   # Apply another linear transformation to the permuted tensor without using its output as an input for this second linear function.
        return v2_1


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 4)
__output__   = m(x1)

# Output expected by the user