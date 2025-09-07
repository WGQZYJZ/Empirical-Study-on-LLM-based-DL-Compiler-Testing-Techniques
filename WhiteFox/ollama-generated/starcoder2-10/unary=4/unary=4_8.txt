
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8 * 64 * 64, 10)
 
    def forward(self, x2):
        v7  = F.relu_(x2 + 3) 
        v9  = self.linear(v7)
        return v9


# Initializing the model
m  = Model()
__output__   = m(x1)


