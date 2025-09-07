
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 16)
 
    def forward(self, qk_value, attn_mask=None):
        v1 = self.query(qk_value[0]) # (batch_size, num_heads, seq_len, dim_per_head) @ (seq_len, dim_per_head)
        v2 = torch.matmul(attn_mask, v1) # batch_size x num_heads * attn_mask.sum(-2) + ...
        v3 = self.query(qk_value[1]) # batch_size x (num_heads - 1) * attn_mask.sum(-2) @ dim_per_head.unsqueeze(1)
        v4 = torch.matmul(attn_mask, v3).transpose(0, 1)
        output = torch.cat([v2, v4], dim=-1) # (batch_size, num_heads * attn_mask.sum(-2) + ... -1) @ (seq_len, dim_per_head)
        return output


# Initializing the model
m = Model()
qk = torch.randn(3, 8, 64, 64)
value = torch.randn(3, 2, 64, 64) # value is the input tensor of the self-attention mechanism
output = m((qk, value), attn_mask=torch.randn(3, 64, 64))

