
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5 + (v1 * v1 * v1 * 0.044715) * 0.017854 + (v1 * v1 * v1 * v1 * 0.0993816) * 0.022551
        v3 = torch.tanh(v2) + 1
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(1, 100)
