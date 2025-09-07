
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor1, tensor2):

        v  = torch.cat([tensor1, tensor2], dim=3)
        v = v[0][0]
        v = v * v 
        v = v - v 

        return v


# Initializing the model
m  = Model()
# Inputs to the model
t1  = torch.ones(1, 2, 485, 3)
t2 = t1
__output__  = m(t1, t2)

