
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(40, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 40) # Note that the shape of input_tensor is not a same as that of other and x2's shape is (32,)
other = torch.randn((5,), requires_grad=True) 
