
class Attention(torch.nn.Module):
    def __init__(self, hsz=768, num_heads=12, attn_drop=0., attn_bias='learned'):
        super().__init__()

        self.qkv = torch.nn.Linear(hsz // 3 * (num_heads + 1), 4)
        self.proj = torch.nn.Linear(hsz // num_heads, hsz)
        self._attn_drop = nn.Dropout(attn_drop).type('torch.cuda.FloatTensor')

    def forward(self, x):
        bs = len(x)

        qkv = self.qkv(x) # [b, c*head, 3] -> [b, c//head, 12, 3]
        q, k, v = torch.chunk(qkv, 3, dim=1) # each head has c // n_head
        q = q / math.sqrt(self.qkv.weight[-2].data[0]) # divide q by sqrt of head-dim

        attn_mask = self._attn_mask_func(bs, x).type('torch.cuda.FloatTensor') # [b, 12]

        # each head has c // n_head
        attn_weight = torch.softmax((q @ k.transpose(-2, -1)) + (not self._attn_drop), dim=-1) * \
                      0.975 if not attn_bias else self._attn_bias
        attn_weight *= attn_mask[:, None] # [b, 12, 36]

        attn = attn_weight @ v

        out = self.proj(attn).view(*x.shape[:-1], -1)  # (b, 768)
        return out

m = Attention()


x = torch.randn(50224//3, 768*9)

