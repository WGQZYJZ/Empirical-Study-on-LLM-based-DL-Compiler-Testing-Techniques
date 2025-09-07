class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.Split()
 
    def forward(self, x1):
        splitted  = self.split(x1) 
        concatenated = torch.cat([splitted[0], splitted[2]], dim=1) 
        return concatenated
