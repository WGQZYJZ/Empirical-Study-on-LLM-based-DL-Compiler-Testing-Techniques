
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x):
        v0  = torch.mm(x1, x2)
        v0  = v0  +  v0
        return v0

# Initializing the model
m  = Model(input1=torch.randn(4, 5), input2=torch.randn(4, 5))

 # Inputs to the model
x = torch.rand(7)
 
 