

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self._add_layer(x1)  # Calling custom function to add a new tensor
        return v1
 
    @torch.jit.ignore
    def _add_layer(self, t1): 
        v2  = torch.nn.Linear(t1).forward(other=None, training=True)
        v3 = v2 + self._add_layer(v2) #Adding the result of applying a linear transformation to an input tensor to another tensor (specified by keyword argument "other")
        return v3
 

# Initializing the model 
m = Model()
 
# Input tensors for the model 
x1 = torch.randn(4, 650) #Applying a linear transformation to this input tensor will result in an output tensor with shape [4, 2]
other = torch.ones([4, 3])


__output__  = m(x1)

