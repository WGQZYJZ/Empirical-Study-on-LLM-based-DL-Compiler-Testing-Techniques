
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) * 0.5
        v2 = (v1 * (v1 + 1) * 0.044715) / 3 
        v3 = torch.tanh(v2) + 1
        v4 = v3 * (v3 - v2)
        return v4


# Initializing the model
m = Model()


