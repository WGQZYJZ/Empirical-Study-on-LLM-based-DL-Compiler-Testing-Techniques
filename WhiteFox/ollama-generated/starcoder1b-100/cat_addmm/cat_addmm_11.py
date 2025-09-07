
class Model(torch.nn.Module):
    def __init__(self, num_outputs=1):
        super().__init__()
        self.fc = torch.nn.Linear(20, 4)
 
    def forward(self, x1, x2):
        t1  = torch.addmm(x1, x2, x2)
        t2  = torch.cat([t1], dim=0)
        return t2


# Initializing the model
m = Model()
