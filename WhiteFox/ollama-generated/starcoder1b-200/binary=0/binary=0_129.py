
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v = x1 + other
        return v

 # Initializing the model
m = Model()
 
