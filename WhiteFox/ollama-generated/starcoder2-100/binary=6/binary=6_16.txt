
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other  # Replace 'other' with the name of your input tensor or a random constant/scalar to test the vulnerability.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3,8)
__output__  = m(x1)

# Other inputs to the model
other = 90 # Replace 'other' with another tensor of the same shape and size as x1 or a random constant/scalar

