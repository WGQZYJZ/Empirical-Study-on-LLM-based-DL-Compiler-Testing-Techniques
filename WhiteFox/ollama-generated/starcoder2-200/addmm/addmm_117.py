
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, inp=None): 
        v1 = torch.mm(input1, input2)
        return v1 + inp

# Initializing the model 
m = Model()
 
# Input tensors to the model
input1  = torch.randn(3, 5)
input2  = torch.randn(5, 7)
 
# The 'inp' keyword argument is None (default value), and hence an error will be encountered. Let's change it.
__output__  = m(input1, input2, inp=torch.ones((3, 7)))
