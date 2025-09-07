
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self):
         v1 = torch.full([5, 2], 0)
         v2 = torch.full([7, 3], 8)
         v3 = v1 + v2
         return None


# Initializing the model
m  = Model()

# Inputs to the model
__output__  = m()
