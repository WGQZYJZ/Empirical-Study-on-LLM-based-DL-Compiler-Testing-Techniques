
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1):
        v1 = torch.cat([t1, t1[:, 0:9223372036854775807]], dim=1)
        v2 = v1[:, 0:size] 
        return v2


# Initializing the model