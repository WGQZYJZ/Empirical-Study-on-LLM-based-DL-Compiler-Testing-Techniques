
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        return torch.full([arg1, arg2], 1)

 # Initializing the model
m = Model()

 # Inputs to the model
arg1 = 1
arg2 = 2
