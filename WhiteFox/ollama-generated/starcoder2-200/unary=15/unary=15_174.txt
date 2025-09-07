
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # (1)
        t2 = torch.relu(x1)  # (4a)
        return t2  # (5)
 

