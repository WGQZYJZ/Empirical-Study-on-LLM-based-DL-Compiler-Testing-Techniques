
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=8, max_position_embeddings=512, dropout_p=0.1):
        super().__init__()
        self.num_attention_heads = num_attention_heads
        self.max_position_embeddings = max_position_embeddings
        self.dropout_p = dropout_p
 
        self.embedding = torch.nn.Embedding(vocab_size, hidden_dim)
        self.self_attn = torch.nn.MultiheadAttention(
            num_attention_heads=num_attention_heads,
            dim_key=hidden_dim,
            dim_value=hidden_dim,
            dropout=dropout_p
        )
        self.fc = torch.nn.Linear(hidden_dim, vocab_size)

    def forward(self, input):
        # Shape of inputs: (batch_size, seq_len, hidden_dim)
        batch_size = input.shape[0]
        seq_len = input.shape[1]

        # Shape of input tensor before the embedding layer is applied: (batch_size, seq_len, vocab_size)
        x = self.embedding(input[:, 0])  # Embedding layer
        x = self.dropout(x)  # Dropout to avoid overfitting

        # Shape of input tensor after the embedding layer is applied: (batch_size, hidden_dim)
        x = x.contiguous().view(-1, self.hidden_dim)

        # Shape of input tensor before the self-attention layer is applied: (batch_size, hidden_dim, seq_len, seq_len)
        # (The last line can be removed if batch_size and seq_len are static dimensions.)
        x = self.self_attn(x, x, x)[0]  # Apply attention mechanism

        # Shape of input tensor after the self-attention layer is applied: (batch_size, hidden_dim)
        x = x.contiguous().view(-1, self.hidden_dim)

        # Shape of output: (batch_size * seq_len, vocab_size)
        out = self.fc(x)  # Pass through a linear transformation to the last layer

        return out


# Initializing the model
m = Model()


