
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        torch.split(input1, 80)
        torch.cat([input2], dim=1)
        
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(457, 32, 96, 96)
x2 = torch.randn(458, 32, 96, 96)
 
__output__  = m(x1, x2)

