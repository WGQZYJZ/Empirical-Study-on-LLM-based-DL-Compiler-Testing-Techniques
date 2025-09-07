
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2): 
        v1 = torch.full([arg1, arg2], 1)
        v2 = convert_element_type(v1, dtype='double')
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
arg1 = random.randint(100, 150) # Create a tensor of the specified shape that is filled with random integers between 100 and 150
arg2 = arg1 + random.randint(10, 60) # Select the size of the specified tensor at random from within the specified range
x3  = torch.randn([arg1, arg2])


# Model with different inputs