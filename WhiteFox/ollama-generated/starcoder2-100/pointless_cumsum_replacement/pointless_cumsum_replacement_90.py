
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2):
         t1 = torch.full([arg1, arg2], 1)
         t2 = torch.cumsum(t1, 0)
         return t2

# Initializing the model with different inputs and outputs
m = Model()

 # Inputs to the model
a1 = 4
a2 = 6
