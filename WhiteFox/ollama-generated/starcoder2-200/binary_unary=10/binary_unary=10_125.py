
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) + self.other 
        return F.relu(v1)
        
# Initializing the model
m = Model()

