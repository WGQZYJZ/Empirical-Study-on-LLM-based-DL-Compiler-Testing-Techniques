
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2400, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        return v2


# Initializing the model with initial input data and tensor of arbitrary value that is not used by the model:
m = Model()  # m is an initialized torch module without a "real" forward pass.
 
# Inputs to the model
x1  = torch.randn(30, 2400)
other_tensor = torch.randn(30, 8)

