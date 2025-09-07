
class Model(torch.nn.Module):
    def __init__(self, vocab_size=49152, hidden_dim=64, num_attention_heads=8, dropout_p=0.3):
        super().__init__()

        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.num_attention_heads = num_attention_heads
        self.dropout_p = dropout_p
        self.transformer = nn.Transformer(
            d_model=self.hidden_dim,
            nhead=self.num_attention_heads,
            dim_feedforward=2 * hidden_dim)

        self.query = torch.nn.Linear(vocab_size, hidden_dim)  # Input to the transformer
        self.key   = torch.nn.Linear(vocab_size, hidden_dim)  # Key from the transformer
        self.value = torch.nn.Linear(vocab_size, hidden_dim)  # Value from the transformer

        self.dropout_qkv = nn.Dropout(self.dropout_p)

    def forward(self, x1):
        query = self.query(x1)
        key    = self.key(x1)
        value  = self.value(x1)

        # Query-Key dot product
        qk   = torch.matmul(query, key).transpose(-2, -1)  # Shape: (B, K, N)
        attn_mask = create_attention_mask((qk ** 2).sum(-1), max_len=x1.size(-1)).unsqueeze(1).float()  # Shape: (B, 1, N, N)

        # Dropout on the scaled dot product and add an attention mask
        qk = self.dropout_qkv(qk)
        attn_mask = self.dropout_p * attn_mask  # No dropout here to save memory
        attn_weight = torch.softmax(qk, dim=-1)  # Softmax on the result
        attn_weight = (attn_weight * attn_mask).unsqueeze(-1)  # Attn weights * Mask

        # Value dot product with attention weights
        output = torch.matmul(value, attn_weight)  # Shape: (B, V, N)

        return output


# Initializing the model
m = Model()


