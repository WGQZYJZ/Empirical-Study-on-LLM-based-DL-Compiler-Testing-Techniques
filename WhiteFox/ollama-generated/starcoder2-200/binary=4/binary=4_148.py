
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2

# Initializing the model and setting the "other" tensor
m = Model()
other = torch.randn([3], dtype=torch.float64)
__output__  = m(x1)

