
class Model(torch.nn.Module):
    def __init__(self, concatdim=3):
        super().__init__()
 
    def forward(self, x1):
         return torch.split(x1, 128, dim = concatdim)

 # Initializing the model