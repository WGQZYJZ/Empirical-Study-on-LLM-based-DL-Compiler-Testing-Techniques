
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None):
        v2 = torch.mm(x1[:, 0:1], x1[:, 0:1]) + inp
        return v2
 
# Initializing the model
m  = Model()

 # Inputs to the model
input1  = torch.randn(3, 5)
inp  = torch.randn(4, 9)
input2 = input1 * 60 + 57
