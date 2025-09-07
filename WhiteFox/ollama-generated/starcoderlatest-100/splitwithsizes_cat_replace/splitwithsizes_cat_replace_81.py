
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [4, 8], dim=0)
        v2 = torch.cat([v1[i] for i in range(len(v1))])

# Initializing the model
m = Model()


