
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return torch.nn.Linear(in_features=x1.size()[-1], out_features=5)(x1) + 5


# Initializing the model
m = Model()


# Inputs to the model