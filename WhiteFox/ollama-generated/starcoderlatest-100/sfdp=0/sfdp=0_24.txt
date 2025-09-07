
class Attention(torch.nn.Module):
    def __init__(self, dim_head):
        super().__init__()

        self.dim_head = dim_head  # set to 64 in default
        
        self.qkv = torch.nn.Linear(768, dim_head * 3)

    def forward(self, x):
        bsz, length, _ = x.shape

        qkv = self.qkv(x).reshape(-1, bsz, self.dim_head, 3)
        q, k, v = qkv[...,:3], qkv[..., 3:6], qkv[..., 6:]

        attn = (q @ k.transpose(-2, -1)) / math.sqrt(self.dim_head)
        attention_weights = torch.softmax(attn, dim=-1)
        output = attention_weights.matmul(v)

        return output
# Initializing the model
m = Attention(64)

x = torch.randn(1, 768, 3000, requires_grad=True)
