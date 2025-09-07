
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.split(x1, [360], 0) 
        return torch.cat([v2[i] for i in range(len([360]))], dim=0)

 # Initializing the model
 m = Model()

 # Inputs to the model 
 x1 = torch.randn(79584, 1)
 
 