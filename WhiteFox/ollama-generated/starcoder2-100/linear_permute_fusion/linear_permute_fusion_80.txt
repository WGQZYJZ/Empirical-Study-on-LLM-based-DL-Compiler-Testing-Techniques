
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(-3, -2)
        return v2

# Initializing the model 
m = Model()
__output__  = m(torch.randn(10, 5, 4))

