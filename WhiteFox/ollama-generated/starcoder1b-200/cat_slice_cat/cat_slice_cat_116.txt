
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = v1[:, 0:size]
        v3 = torch.cat((v1[0:8], v2[0:8]), dim=1)
        return v3


# Initializing the model
m = Model()


