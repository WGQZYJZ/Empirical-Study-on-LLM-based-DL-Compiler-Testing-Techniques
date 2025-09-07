
class Model(torch.nn.Module):
    def __init__(self, arg1=3072, arg2=64):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([arg1, arg2], 1)
        v2  = convert_element_type(v1, torch.int8) # Convert the elements of the tensor to dtype `torch.int8`
        v3  = torch.cumsum(v2, 1)
        return v3

# Initializing the model
arg1  = int(os.getenv('ARG1', '3072'))  # Specify the first argument for model.forward() function; default value is `int(os.getenv('ARG1', '3072'))`
arg2  = int(os.getenv('ARG2', '64'))    # Specify the second argument for model.forward() function; default value is `int(os.getenv('ARG2', '64'))`
m     = Model(arg1, arg2)               # Create an instance of this class with specified arguments

