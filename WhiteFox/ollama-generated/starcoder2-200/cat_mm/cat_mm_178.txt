
class Model(torch.nn.Module):
    def __init__(self, d1=5048):
        super().__init__()
        self.fc  = torch.nn.Linear(d1*3, d1)
 
    def forward(self, x1):
        v1  = torch.mm(x1, self.fc.weight.t()) 
        v2  = torch.cat([v1, v1, ..., v1]) # Concatenation of the result tensor along a certain dimension
        return v2


# Initializing the model
m = Model()

