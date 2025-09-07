
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 32)
        v2 = [v3 for i in range(len(v1))]
 
        return torch.cat(v2, dim=0),  # Note that there is a missing comma in this line

# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(4976, 3)

