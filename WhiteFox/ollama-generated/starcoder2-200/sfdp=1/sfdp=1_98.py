
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(
            data=torch.ones([]) * 0, requires_grad=True)
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, query, key, value, scale_factor):
        v1  =  torch.matmul(query, key.transpose(-2, -1))
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3) + 1
        v2  = self.scale * scale_factor # Scale the dot product by the inverse scale factor
        v5 = torch.nn.functional.dropout(v2, p=0.5)
        return v4

