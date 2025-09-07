
class MultiHeadAttnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, x1, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask  # (B, Tq, Tk, Ckv * nH) @ (B, Ckv, Tkv, Dkv) -> (B, Tq, Tk, nHv)
        _, attn_weight = self.attn(qk, qk, qk)  # Softmax to the scaled dot product of query and key
        output = attn_weight @ value  # Weighted sum with attention mask
        return output
