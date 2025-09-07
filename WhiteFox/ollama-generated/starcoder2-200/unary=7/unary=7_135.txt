
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        v8  = clamp(min=0., max=6., input=v7+3.)
        v9  = v8 / 6.
        return v9

# Initializing the model
m  = Model()
