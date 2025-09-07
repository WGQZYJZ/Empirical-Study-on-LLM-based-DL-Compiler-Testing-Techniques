
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1=320, arg2=960):
        t1  = torch.full([arg1, arg2], 1, dtype='f')
        t2  = torch.nn.functional.convert_element_type(t1, 'f8') # Convert the elements of the tensor to double precision floating point numbers
        t3  = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m  = Model()


# Inputs to the model
arg1 = 640
arg2 = 958 # must be a list
__output__  = m(arg1=arg1, arg2=arg2)



