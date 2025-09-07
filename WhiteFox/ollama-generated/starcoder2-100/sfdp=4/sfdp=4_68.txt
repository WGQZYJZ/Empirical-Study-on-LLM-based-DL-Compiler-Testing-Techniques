
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, attn_mask=None):
        super().__init__()
        self._attn = torch.nn.Linear(2048, 512)
        self._attn_out = torch.nn.Linear(512, 2048)
        self._softmax = torch.nn.Softmax()
 
    def forward(self, q, k, v):
        qk = self._attn(q) @ self._attn(k).transpose(-2, -1) / math.sqrt(
            q.size(-1))
        if attn_mask is not None:  # add the mask to the scaled dot product
            qk += attn_mask  # prevent attention to certain positions
        attn = self._softmax(qk)
        out  = self._attn_out(attn @ v)
        return out
