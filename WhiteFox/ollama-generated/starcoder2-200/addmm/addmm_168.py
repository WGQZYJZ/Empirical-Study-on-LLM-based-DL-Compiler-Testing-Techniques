
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, inp=0.5):
       v2 = torch.mm(x1, input1) + 