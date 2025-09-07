
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=torch.ones((4,)), input2=torch.zeros((5,))):
        v1 = torch.mm(x1, input2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

