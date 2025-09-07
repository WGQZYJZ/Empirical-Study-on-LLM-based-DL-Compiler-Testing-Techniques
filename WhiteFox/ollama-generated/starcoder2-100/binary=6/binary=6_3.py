
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = v1 - other 
        return v2


# Initializing the model