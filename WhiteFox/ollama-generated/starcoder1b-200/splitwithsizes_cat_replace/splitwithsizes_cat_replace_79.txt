
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # This line can be triggered if `return True` is added
        return torch.split(x1, [64], dim=0)[0]
 

# Initializing the model
m = Model()


