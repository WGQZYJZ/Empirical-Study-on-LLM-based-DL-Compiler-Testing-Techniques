
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mmt  = torch.nn.Linear(50, 1)
 
    def forward(self, inp):
        v1  = torch.mm(inp.float(), inp2.float())
        v4  = v1 + inp 
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
input1 = torch.randn(50)
input2 = torch.randn(50)
inp = torch.randn(1, )
