
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4)
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v8  = (v7 > 0).float() 
        v9  = v7 * negative_slope
        v10 = v8 * t1 + (~v8) * t3
        return v10

# Initializing the model
n = Model()

