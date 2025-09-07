
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1, y2) 
        v2 = torch.mm(y2, x1)
        return torch.sum([v1 + v2], dim=0).data
    
    return model


# Initializing the model and feeding the inputs into it