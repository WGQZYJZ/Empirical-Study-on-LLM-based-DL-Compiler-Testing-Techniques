
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):  # Two inputs to this model
        t1 = torch.mm(input1, input2) 
        t2 = torch.cat([t1] * 3, dim=0)
        return t2


# Initializing the model
m = Model()


# Inputs to the model