
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Note that this function is added to a newly generated model class by users' source code
        t1 = self._modules['conv'](x1)  
        v2  = t1 - other # This pattern can be used for the first time to construct a new PyTorch model
        v3  = torch.nn.functional.relu(v2) 
        return v3


# Initializing the model and defining the value of "other" variable which is used in the forward function above.
m  = Model()
other = torch.randn([])

# Input tensors to the model 
x1 = torch.randn(1, 4, 200, 200) # Note that the shape may be different from what the user needs (e.g., (3, 8, 64, 64))
__output__  = m(x1)

