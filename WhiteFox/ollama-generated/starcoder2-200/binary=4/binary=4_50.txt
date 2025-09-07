
class Model(torch.nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, 8)
 
    def forward(self, x1):
        v2 = self.linear(x1) + other
        return v6


# Initializing the model
m = Model(3072)
 
# Inputs to the model
x1 = torch.randn(32, 3072)
__output__  = m(x1)

