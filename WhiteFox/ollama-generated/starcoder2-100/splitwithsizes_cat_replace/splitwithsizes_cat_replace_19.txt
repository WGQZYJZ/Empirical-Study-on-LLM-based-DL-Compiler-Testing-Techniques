
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       v = torch.split(x1, 503, dim=1) 
       return torch.cat([v[i] for i in range(len(v))], dim=1)


# Initializing the model