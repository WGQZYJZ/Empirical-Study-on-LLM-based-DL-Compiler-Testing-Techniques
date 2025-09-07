
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(**kwargs)
 
    def forward(self, x1, x2):
        output = self.attention(x1, x2)[0]
        return output
