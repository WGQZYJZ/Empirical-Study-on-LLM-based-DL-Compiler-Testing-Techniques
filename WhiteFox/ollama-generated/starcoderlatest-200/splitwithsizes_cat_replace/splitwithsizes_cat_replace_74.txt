
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v  = torch.split(x1, 2048, dim=0)
        concatenated_tensor  = torch.cat([v[i] for i in range(len(v))], dim=0)
        return concatenated_tensor

