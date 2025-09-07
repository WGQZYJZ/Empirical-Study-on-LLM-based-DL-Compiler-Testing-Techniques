
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=1, num_heads=2)
 
    def forward(self, qk, v1, v2):
        q  = torch.unsqueeze(qk, dim=-1)
        k  = torch.unsqueeze(qk, dim=-2)
        v  = torch.unsqueeze(v1, dim=0)
        v2 = torch.unsqueeze(v2, dim=-3)

        