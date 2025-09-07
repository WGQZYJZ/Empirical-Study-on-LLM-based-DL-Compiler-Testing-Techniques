
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v2  = torch.mm(x1[0], x1[1]) 
        return v2 + torch.mm(x1[2], x1[3])

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = [torch.randn(64,64), torch.randn(50,78)]
x2  = (torch.randn(35,79), torch.randn(24,77))
 
# Initializing the inputs with shapes different from those used in Model
input1  = [[x1[i], x2[j]] for i, j in zip([0]*64+[1]*50 + [2]*35 + [3]*24, range(78))]
__output__  = m(input1)

