
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(256,1)
 
    def forward(self, x3):
        v7= x3  *0.5
        v8= x3  *0.7071067811865476
        v9=torch.erf(v8)
        v10= v9+1
        return v7*v10


# Initializing the model