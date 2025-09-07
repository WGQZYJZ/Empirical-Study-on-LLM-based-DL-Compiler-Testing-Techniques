
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 8)

    def forward(self, x):

        v1 = self.linear(x)
        v2 = v1 + other_tensor # "other" is an example of the keyword argument to be replaced by the user
        
        return v2

# Initializing the model
m = Model()

# Inputs to the model
input = torch.randn(8, 1024)


__output__  = m(input)