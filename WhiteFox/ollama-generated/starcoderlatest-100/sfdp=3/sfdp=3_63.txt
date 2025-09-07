
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, qk):
        attn_output = self.attn(qk[0], qk[1], qk[2])
        return attn_output[0]
