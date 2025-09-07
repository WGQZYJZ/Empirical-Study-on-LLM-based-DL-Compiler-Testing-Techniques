
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): # The new input tensor x3 will be a parameter of this function
        v1  = self.linear(x1)
        v2  = v1 - other  # In this example, 'other' is a parameter in this forward function
        v3  = torch.relu(v2)
        return v3
 

# Initializing the model