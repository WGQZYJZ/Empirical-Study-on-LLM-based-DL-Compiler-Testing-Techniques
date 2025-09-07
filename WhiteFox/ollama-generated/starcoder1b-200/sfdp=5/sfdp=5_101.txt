
class Model(torch.nn.Module):
    def __init__(self, query_size, key_size, embedding_size, num_heads, padding_idx=None):
        super().__init__()
        self.query  = torch.nn.Linear(query_size, embedding_size)
        self.key    = torch.nn.Linear(key_size, embedding_size)
        self.value  = torch.nn.Linear(embedding_size, query_size)
        self.fc     = torch.nn.Linear(num_heads * embedding_size, num_heads * query_size)
        if padding_idx is not None:
            self.padding_idx = torch.nn.Embedding(vocab_size=padding_idx + 2, num_embeddings=embedding_size)
 
    def forward(self, x1):
        query = self.query(x1).view(-1, self.num_heads, self.head_dim).transpose(0, 1)  # Project the input of the convolution to the representation
        key   = self.key(x1).view(-1, self.num_heads, self.head_dim).transpose(0, 1)
        value = self.value(x1).contiguous().view(-1, self.query_size)
        attn = torch.matmul(attn_weights, query).contiguous()
        attn = attn.view(attn.shape[0], -1, attn.shape[-1])  # Re-project the attention weights to match the shape of the input to the attention mechanism
        attn = self.fc(torch.nn.functional.dropout(attn, dropout_p, True))
        attn = torch.matmul(attn, key).contiguous()  # Projecting the attention weight back to the representation
        out  = torch.matmul(value, attn)                   # Computing the output
        return out


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
