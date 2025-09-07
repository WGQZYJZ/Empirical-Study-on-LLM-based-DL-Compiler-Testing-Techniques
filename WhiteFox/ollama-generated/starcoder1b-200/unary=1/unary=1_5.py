
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 256)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5 + ((v1  * v1) * 0.044715) + ((v1  * v1  * v1) * 0.096381) + ((v1  * v1  * v1  * v1) * 0.0024928)
        v3 = torch.tanh(v2)
        v4 = v3 + 1
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
