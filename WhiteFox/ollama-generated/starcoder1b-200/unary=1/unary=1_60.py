
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48, 10)
 
    def forward(self, x):
        v1 = self.linear(x) * 0.5
        v2 = (self.linear(x) + (self.linear(x) * self.linear(x)) * 0.044715) * 0.7978845608028654
        v3 = torch.tanh(v2) + 1
        return v3


# Initializing the model
m = Model()


