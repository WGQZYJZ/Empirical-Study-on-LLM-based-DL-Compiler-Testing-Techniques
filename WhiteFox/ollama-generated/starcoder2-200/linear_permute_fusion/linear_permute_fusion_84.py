
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v  = v.permute(0, 2, 1)
        return v

# Initializing the model
m  = Model()

 # Inputs to the model
    x1 = torch.randn(3 , 4, 5)

    __output__  = m(x1)

