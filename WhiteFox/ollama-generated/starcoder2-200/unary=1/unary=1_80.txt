
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v3  = self.linear(x2)
        v6  = t1 + (v3 * v3 * v3) * 0.044715
        v9  = v6  * 0.7978845608028654 
        v10 = torch.tanh(v9) 
        v11 = v10 + 1
        return v3*v11


# Initializing the model:
m = Model()

 # Inputs to the model