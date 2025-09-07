
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 3)
        self.linear2 = torch.nn.Linear(9, 5)
 
    def forward(self, x1):
        v1 = self.linear1(x1) + other 
        return v1
