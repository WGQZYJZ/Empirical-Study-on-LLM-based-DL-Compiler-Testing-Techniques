
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1[:, :4], x2[:, :3]], dim=1)
        v2 = torch.cat([v1[:, :64], v1[:, 9:]], dim=1)
        return v2


# Initializing the model
m = Model()

