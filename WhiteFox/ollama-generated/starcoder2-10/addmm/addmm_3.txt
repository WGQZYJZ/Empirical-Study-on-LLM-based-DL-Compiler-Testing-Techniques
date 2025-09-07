
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, input2):
        v0 = torch.mm(input1, input2) 
        return v0 + inp


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn((3,5)) # A random tensor with size 3x5 for input1
input2 = torch.randn(5,7)# A random tensor with size 5x7 for input2
