
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp): # passing the tensor to the model by keyword argument 'inp' in forward() method
        v1 = torch.mm(x1, x2)
        return v1 + inp

# Initializing the model
m  = Model()

 # Inputs to the model: 'x1' and 'inp' are tensors. 'x2' is the tensor to be passed as a keyword argument in the forward() method of the module.  
x1, x2,  input_tensor,  inp  = torch.randn(30),  torch.randn(54, 90)

 # Initializing the model and feeding tensors to it. 'inp' is passed as a keyword argument in the forward() method of the module.
__output__  = m(x1, x2, input_tensor=inp)
