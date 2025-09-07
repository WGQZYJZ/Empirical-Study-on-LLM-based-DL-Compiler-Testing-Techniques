
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2):
        super().__init__()
        self.cumsum = torch.cumsum
        self._tensor = torch.full([arg1, arg2], 1)
 
    def forward(self, x): 
        v1 = self.cumsum(self._tensor, dim=1).convert_element_type(torch.float32) # Create a tensor filled with the scalar value 1 along dimension 0
        return v1


# Initializing model with 4 and 8 as arguments of cumsum
m = Model(4, 8)

# Inputs to the model