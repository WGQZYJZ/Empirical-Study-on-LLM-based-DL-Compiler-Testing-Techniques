
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2  = v1 + other  # This is the new pattern that does not match with the previous one
        
        return v2
 
# Initializing the model