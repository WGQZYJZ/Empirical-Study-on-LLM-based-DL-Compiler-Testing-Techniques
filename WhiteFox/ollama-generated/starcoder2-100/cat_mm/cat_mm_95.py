
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
 
    def forward(self,  input1,  input2):
        v1 = torch.mm(input1, input2)
        v3 = torch.cat([v1] * 5 + [v1], -1)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(10, 48, 48) 
 x2  = torch.randn(96, 50, 50)
 
 __output__  = m(x1, x2)