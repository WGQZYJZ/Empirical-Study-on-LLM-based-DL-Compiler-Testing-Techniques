
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, inp = torch.tensor([2])):
        v1  = torch.mm(x1, x1) + inp 
        return v1

