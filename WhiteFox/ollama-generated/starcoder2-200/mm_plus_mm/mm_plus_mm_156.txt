
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()

    def forward(self, x1, y1, z1): 
        return torch.mm(x1,y1)+z1

# Initializing the model 
m = Model(input1, input2) 

# Inputs to the model
x1 = torch.randn(3,5)
y1 = torch.randn(5,4)
z1 = torch.randn(3,5)
__output__  = m(x1, y1, z1)

