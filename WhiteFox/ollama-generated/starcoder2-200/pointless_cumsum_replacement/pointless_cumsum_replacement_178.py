
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        return torch.full([4, 3], 1)
 
m = Model()
 
print(m())

