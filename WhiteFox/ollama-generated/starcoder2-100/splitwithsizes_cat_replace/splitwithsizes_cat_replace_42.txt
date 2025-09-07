
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        a1 = torch.split(x1, 4)
        v2 = torch.cat([a1[i] for i in [3,0]]) # Concatenate the third split tensor with the first one along dimension 1 (the dimension along which `torch.split` and `torch.cat` are performed).
        return v2

m = Model()
