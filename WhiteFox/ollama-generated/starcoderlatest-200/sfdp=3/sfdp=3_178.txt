
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=64, num_heads=8)
 
    def forward(self, qk):
        kq, vq = qk
        output = self.attn(qk[0], vq[0])
        return output


# Initializing the model
m = Model()
qk  = (torch.randn(256, 32, 196), torch.randn(256, 8, 196))
