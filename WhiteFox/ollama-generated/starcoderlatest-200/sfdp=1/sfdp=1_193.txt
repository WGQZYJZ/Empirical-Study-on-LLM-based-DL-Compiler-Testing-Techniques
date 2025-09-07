
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2):
        v1 qlk = self.attention(x1, x2)
        v2 qlv = self.attention(query, value.transpose(-2,-1))
        return v1
