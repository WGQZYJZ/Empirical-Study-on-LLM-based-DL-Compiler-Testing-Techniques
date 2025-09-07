
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return relu(-v1 + 2.5 * (1 / torch.exp(v1))))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
