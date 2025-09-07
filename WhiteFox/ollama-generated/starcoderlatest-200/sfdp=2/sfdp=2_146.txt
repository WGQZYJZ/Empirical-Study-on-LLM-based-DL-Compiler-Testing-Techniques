
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16, num_heads=8)
        self.layer_norm = torch.nn.LayerNorm(dim)

    def forward(self, q, k, v, attn_mask=None):
        qk = self.attention(q, k, v, attn_mask)[0]  # [batch_size x num_heads x seq_length x dim_per_head]

        if attn_mask is not None:
            qk = qk + torch.arange(attn_mask.shape[1], dtype=torch.float32, device=attn_mask.device) * -1e9
            qk = torch.nn.functional.softmax(qk, dim=-1)
        output = self.layer_norm(q + qk.transpose(-2, -1))  # [batch_size x seq_length x dim]

        return output


# Initializing the model
m = Model(512)
# Inputs to the model
query  = torch.randn(16, 8, 32, 64)
key    = torch.randn(16, 8, 64, 64)
value  = torch.randn(16, 8, 64, 64)
attn_mask = torch.rand(16, 32) * -1e9
