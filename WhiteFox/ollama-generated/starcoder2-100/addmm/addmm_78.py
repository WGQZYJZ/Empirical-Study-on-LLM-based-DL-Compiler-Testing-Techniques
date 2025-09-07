
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2)
        v3  = v1 + inp
        return v3

 # Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(4, 5)
x2  = torch.randn(4, 5)
inp = torch.randn(10).to("cpu")
 
# Initializing the tensor
