
class Model(torch.nn.Module):
    def __init__(self, embedding_dim, num_heads=8, hidden_size=1024):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.embedding_proj = torch.nn.Linear(embedding_dim, hidden_size)
        self.query_layer  = torch.nn.TransformerEncoderLayer(num_heads=num_heads, hidden_size=hidden_size, dropout=0.1)
        self.key_value_layer = torch.nn.MultiheadAttention(hidden_size=hidden_size, num_heads=num_heads)
    
    def forward(self, query, key, value, attention_mask):
        # Input: [batch x input_seq_len x embedding_dim]
        # Output: [batch x hidden_size]
        hidden = self.embedding(query)
        hidden  = hidden * math.sqrt(hidden.size(-1))
        hidden  = self.embedding_proj(hidden)

        # Input: [batch x input_seq_len x hidden_size]
        # Output: [batch x attention_head x embedding_dim]
        context = torch.matmul(hidden, key.transpose(-2, -1))
        
        # Input: [batch x attention_head x embedding_dim]
        # Output: [batch x input_seq_len x embedding_dim]
        output = torch.matmul(attn_weight, value)

        return output


# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(2, 3, 50, 100) # [batch x input_seq_len x embedding_dim]
key    = torch.randn(2, 64, 50, 100)   # [batch x hidden_size x input_seq_len x input_embedding_dim]
value  = torch.randn(2, 64, 50, 100)   # [batch x hidden_size x input_seq_len x input_embedding_dim]
attention_mask = torch.ones([2, 3, 50, 50]) # [batch x seq_len x seq_len]
