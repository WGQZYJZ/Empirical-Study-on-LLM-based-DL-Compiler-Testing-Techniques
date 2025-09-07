
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split  = torch.split(x1, [32], dim=0)
        return concat = torch.cat([split[i] for i in range(len(split))], dim=0)
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(64, 32, 8, 8)
 
 