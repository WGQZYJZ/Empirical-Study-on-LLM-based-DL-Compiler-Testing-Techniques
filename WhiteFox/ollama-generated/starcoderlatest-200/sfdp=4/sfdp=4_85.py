
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, attn_mask):
        v1 = torch.matmul(qk, key.transpose(-2, -1) / math.sqrt(qk.size(-1))) + attn_mask
        attn_weight = torch.softmax(v1, dim=-1)
        output = attn_weight @ value
        return output
