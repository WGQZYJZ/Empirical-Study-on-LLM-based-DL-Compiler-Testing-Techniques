
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.rand(1))
 
    def forward(self, query, key, value):
        vq  = torch.matmul(query, key.transpose(-2, -1)) / self.scale 
        return vq


m = Model()
