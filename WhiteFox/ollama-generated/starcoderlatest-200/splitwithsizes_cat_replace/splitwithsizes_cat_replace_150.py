
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.split(x1, 2, dim=1), torch.cat(r11, dim=1)
    

