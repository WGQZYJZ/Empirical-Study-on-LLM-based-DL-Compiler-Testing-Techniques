
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(256, 384)
 
    def forward(self, x1):
        v1  = self.lin(x1) 
        v2  = v1 + other  # add another tensor to the output of the linear transformation
        v3  = torch.relu(v2) 
        return v3


# Initializing model