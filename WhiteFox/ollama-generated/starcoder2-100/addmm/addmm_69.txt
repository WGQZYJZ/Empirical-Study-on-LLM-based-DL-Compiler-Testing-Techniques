
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v0 = torch.mm(x1,inp)  # Matrix multiplication
        return v0 + inp


# Initializing the model
m = Model()
 
# Inputs to the model