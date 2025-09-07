
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 10
 
    def forward(self, query, key, value):
        v3 = torch.matmul(query, key.transpose(-2, -1))
        v4 = v3 * scale_factor
#        v5 = torch.nn.functional.softmax(v4, dim=-1)
        return v6

