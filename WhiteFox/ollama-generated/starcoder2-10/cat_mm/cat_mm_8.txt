
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x1[3])
        v2  = torch.cat([v1] * 4 + [v1] * 5) 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
__output__  = m(x1)

