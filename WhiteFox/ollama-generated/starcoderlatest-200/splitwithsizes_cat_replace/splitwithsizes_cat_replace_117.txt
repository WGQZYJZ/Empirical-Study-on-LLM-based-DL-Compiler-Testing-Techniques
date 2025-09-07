
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 256, dim=3)
        v2 = [0] * len(v1)
        for i in range(len(v1)):
            tmp_tensor = torch.cat([v1[i]], dim=3)
            v2[i] = torch.cat([tmp_tensor], dim=3)
        concatenated_tensor = torch.cat(v2, dim=0)
        return concatenated_tensor


# Initializing the model
m = Model()

