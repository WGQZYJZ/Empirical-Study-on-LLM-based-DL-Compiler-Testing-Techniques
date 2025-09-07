
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) 
        v2 = torch.cat([v1] * 3, dim=0) 
        return v2

# Initializing the model
m = Model(dim=1) # Change the dimension value to meet the needs of the user.
