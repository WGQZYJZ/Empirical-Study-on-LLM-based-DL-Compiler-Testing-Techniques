
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear_1.weight, self.linear_1.bias)
        v2 = self.linear_2(v1)
        return v2
# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 2, 2)
 