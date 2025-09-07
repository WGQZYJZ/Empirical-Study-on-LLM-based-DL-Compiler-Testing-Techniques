
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): # We want to test that the model is different from before. Hence we take inputs which are not the same as before.
        v3 = torch.mm(x1, x2) + 0.5
        return v3


# Initializing the model
m = Model()


# Inputs to the model