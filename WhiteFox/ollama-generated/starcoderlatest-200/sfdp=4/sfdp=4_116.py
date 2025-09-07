
class Attention(torch.nn.Module):
    def __init__(self, num_attention_heads=8, dim_attention_head=64):
        super().__init__()
        self.num_attention_heads = num_attention_heads
        self.dim_attention_head = dim_attention_head
        self.key_projection = torch.nn.Linear(3, num_attention_heads * dim_attention_head)
        self.value_projection = torch.nn.Linear(3, num_attention_heads * dim_attention_head)

    def forward(self, query, key, value):
        qk = torch.einsum('bhd, bhjd -> bhij', [query, self.key_projection])
        attn_weights = torch.softmax(qk, dim=-1)
        v = torch.einsum('bhij, bhjd -> bhd', [attn_weights, value])
        v = torch.matmul(v, self.value_projection)

        return v


# Initializing the model
m = Attention()
query = torch.randn(4, 3, 64, 64).float()
key = torch.randn(2, 3, 64, 64).float()
value = torch.randn(1, 2, 64, 64).float()
