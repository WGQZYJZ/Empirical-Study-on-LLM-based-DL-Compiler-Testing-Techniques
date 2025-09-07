
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        splitted  = torch.split(x1, [32], dim=0) 
        concatenation = torch.cat([splitted[i] for i in range(len(splitted))],dim=0 )
        return concatenation

# Initializing the model
m = Model()

