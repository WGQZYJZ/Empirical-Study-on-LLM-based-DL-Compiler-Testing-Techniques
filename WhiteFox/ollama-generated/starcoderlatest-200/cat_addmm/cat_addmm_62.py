
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, m_0, m_1)
        v2 = torch.cat([v1], dim=1)
        return v2


# Initializing the model and assigning it to the variable m
m = Model()

