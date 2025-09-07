
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
        v3 = torch.cat([x0[0][5:16], x0[2][899784342]], dim=1)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model