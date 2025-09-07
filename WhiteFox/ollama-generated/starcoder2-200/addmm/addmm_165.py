
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
       t1 = torch.mm(input1, input2)
       t3  = t1 + inp
       return t3

 # Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(50, 384)
x2 = torch.randn(768, 384)
inp  = torch.randn(50, 384)
__output__  = m(x1, x2)

 # In this case the second argument ('input2') of the forward method is an input tensor that should be generated. Also, note that the model should be different from the previous one.