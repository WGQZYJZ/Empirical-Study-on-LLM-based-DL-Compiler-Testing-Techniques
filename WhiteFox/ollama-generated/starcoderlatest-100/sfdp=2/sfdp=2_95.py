
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(embed_dim=64, num_heads=1)
 
    def forward(self, qk, v, k):
        # Attention
        attn = self.attn(qk, k, v)

        return attn


# Initializing the model
m = Model()
 
# Inputs to the model
qk  = torch.randn(1, 32, 1024, 64) # shape (batch_size, num_heads, qk_len, k_len), where query shape is (batch_size, embed_dim, qk_len) and key shape is (batch_size, embed_dim, k_len)
v = torch.randn(1, 32, 1024, 64) # shape (batch_size, num_heads, v_len, k_len), where value shape is (batch_size, embed_dim, v_len) and key shape is (batch_size, embed_dim, k_len)
k = torch.randn(1, 32, 1024, 64) # shape (batch_size, num_heads, qk_len, k_len), where query shape is (batch_size, embed_dim, qk_len) and key shape is (batch_size, embed_dim, k_len)
