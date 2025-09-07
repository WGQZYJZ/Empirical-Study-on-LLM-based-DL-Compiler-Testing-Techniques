
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(256, 8)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, attn_mask: torch.Tensor, dropout_p=0.1):
        v, weight = self.attn(query, key, key + attn_mask)
        return v


# Initializing the model
m  = Model()


# Inputs to the model

q = torch.randn(8, 32, 256).cuda()
k = q
m1 = torch.ones((8, 32), dtype=torch.bool)
attn_mask = -1000 * (1.0 - m1[:, None])

 