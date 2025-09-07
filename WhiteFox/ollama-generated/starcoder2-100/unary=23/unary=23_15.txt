
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model