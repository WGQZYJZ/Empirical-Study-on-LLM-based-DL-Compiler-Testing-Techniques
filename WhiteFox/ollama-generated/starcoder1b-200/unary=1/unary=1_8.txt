
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v  = self.linear(x)
        return v * 0.5 + (v ** 2) * 0.044715 + (v ** 3) * 0.7978845608028654 + torch.tanh(v)


# Initializing the model
m = Model()


