
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v4  = v3.permute(-2,-1)
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1= torch.randn(5000000,)


