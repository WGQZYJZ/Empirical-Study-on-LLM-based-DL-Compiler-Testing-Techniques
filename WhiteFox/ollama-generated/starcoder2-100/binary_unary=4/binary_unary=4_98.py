
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) 
        v2  = v1 + other 
        v3  = F.relu(v2) # or nn.ReLU()
        return v3


# Initializing the model