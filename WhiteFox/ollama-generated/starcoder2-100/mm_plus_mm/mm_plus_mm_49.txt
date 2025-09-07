
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v1  = torch.mm(x1,y1)
        return v1

 # Initializing the model
m  = Model()

 # Inputs to the model