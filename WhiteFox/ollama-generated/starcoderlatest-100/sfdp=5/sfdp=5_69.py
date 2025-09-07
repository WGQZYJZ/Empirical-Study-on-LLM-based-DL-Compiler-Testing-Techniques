
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=4):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 12 * num_attention_heads) # (batch_size, seq_length, embedding_dim) -> (batch_size, seq_length, num_attention_heads*embedding_dim)
        self.attn_pool = torch.nn.AdaptiveAvgPool2d((1, 1)) #(batch_size, seq_length, embedding_dim) -> (batch_size, embedding_dim)
        self.linear2 = torch.nn.Linear(12 * num_attention_heads, 4) # (batch_size, seq_length, embedding_dim) -> (batch_size, seq_length, out_dim)

    def forward(self, x):
        v1 = x.transpose(-2, -1).contiguous().view(x.shape[0], -1, 8).permute(0, 3, 2, 1) # (batch_size, embedding_dim, seq_length) -> (batch_size, num_attention_heads*embedding_dim, seq_length)
        v2 = self.linear1(v1) # (batch_size, num_attention_heads*embedding_dim, seq_length) * (batch_size, num_attention_heads*embedding_dim, out_dim) -> (batch_size, seq_length, out_dim)
        v3 = self.attn_pool(v2).squeeze(-1) # (batch_size, seq_length, embedding_dim) * (batch_size, num_attention_heads*embedding_dim, embedding_dim) -> (batch_size, seq_length)
        v4 = self.linear2(v3) # (batch_size, seq_length, out_dim) * (batch_size, seq_length, out_dim) -> (batch_size, seq_length, 16)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # (batch_size, input_dim, seq_len, feature_dim)
