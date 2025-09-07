
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1

# Initializing the model
m  = Model()
other = torch.randn([64], dtype=torch.float32) # random other tensor

# Inputs to the model
x1 = torch.randn(1, 64)

# Setting the value of `other` in the model's parameter space
setattr(m, 'other', other)

__output__  = m(x1)

