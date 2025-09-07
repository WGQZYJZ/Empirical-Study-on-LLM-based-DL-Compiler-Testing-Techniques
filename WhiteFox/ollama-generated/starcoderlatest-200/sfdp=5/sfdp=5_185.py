
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(128, 64)
 
    def forward(self, qk, v):
        _, attn_weight = self.attn(qk, qk, qk, need_weights=True)
        output = attn_weight @ v
        return output
