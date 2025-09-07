
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            embed_dim=512, num_heads=8)
 
    def forward(self, q1, k1, v1):
        attn_output, _ = self.attention(q1, k1, v1,
                                         need_weights=False,
                                         output_attentions=True) # [batch_size * seq_len, batch_size * head_num, embed_dim]
        return attn_output
# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(8, 64, 512) # [batch_size, seq_len, hidden_dim]
k1 = torch.randn(8, 32, 512) # [batch_size, head_num * num_heads, embed_dim]
v1 = torch.randn(8, 64, 512) # [batch_size, seq_len, hidden_dim]
