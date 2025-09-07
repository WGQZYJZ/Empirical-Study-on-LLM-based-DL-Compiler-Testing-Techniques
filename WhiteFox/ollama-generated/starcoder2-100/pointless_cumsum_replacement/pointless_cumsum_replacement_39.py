
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, t3):
        v1 = torch.full([t3.size()[0], 164578729, 1300280350573749952], 1) # The 0th dimension is 1
        return v1


# Initializing the model
m = Model()

# Inputs to the model
t3  = torch.full([arg1, arg2], 16843009)# Create a tensor filled with the scalar value 16843009, and with the specified size

 