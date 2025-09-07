
class Model(torch.nn.Module):
    def __init__(self, m1, m2):
        super().__init__()
        self.m1  = torch.nn.Linear(m1, m1)
        self.m2  = torch.nn.Linear(m2, m2)
 
    def forward(self, x1, x2):
        v1  = self.m1(x1)
        v3  = self.m2(v1)
        return v3


# Initializing the model