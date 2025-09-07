
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x20, y84):
        v93 = torch.cat((x20,y84), 1) 
        size = 7
        v95 = torch.split(v93,size)[-1] 
        return v95


# Initializing the model