
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, x2): # Concatenate the result tensor along a certain dimension
        v1  = torch.mm(x1, x2) 
        v2  = torch.cat([v1] * 5 + [torch.tensor(0)], dim=3)
        return v2
# Initializing the model
m = Model()

