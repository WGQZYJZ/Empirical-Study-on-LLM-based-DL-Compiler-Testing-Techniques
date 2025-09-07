
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 3, 1, 2)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 4, 6) # 5 samples with four input variables each.
__output__  = m(x1)