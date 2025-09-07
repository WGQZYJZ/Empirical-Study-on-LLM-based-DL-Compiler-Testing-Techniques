
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v  = self.linear(x)
        v  = v  * 0.5
        v += (v  * v  * v) * 0.044715
        v *= 0.7978845608028654
        v = torch.tanh(v) + 1
        return v


# Initializing the model
m = Model()


