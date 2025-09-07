
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg0, arg1):
        v1  = torch.full([arg0, arg1], 1) # Create a tensor filled with the scalar value 1, with 2d shape of [arg0, arg1]
        v2  = convert_element_type(v1, torch.float32) 
        v3  = torch.cumsum(v2, dim=1).contiguous()  # Compute the cumulative sum of the elements of the tensor along dimension 1 in float32
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model
arg0_val = random.randint(-50,50) # A random int value between -50 and 50
arg1_val = random.randint(-50,50) # A random int value between -50 and 50
x1  = (random.uniform(0, 3).item(), torch.device('cpu'))

