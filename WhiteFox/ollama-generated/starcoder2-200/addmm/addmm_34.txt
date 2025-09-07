
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v = torch.mm(x1, x2) 
        return  v + inp

 # Initializing the model