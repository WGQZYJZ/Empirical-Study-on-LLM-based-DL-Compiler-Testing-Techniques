
class SelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads

        self.query = torch.nn.Linear(embed_dim, embed_dim)
        self.key = torch.nn.Linear(embed_dim, embed_dim)
        self.value = torch.nn.Linear(embed_dim, embed_dim)

        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x):
        batch_size, num_heads, seq_len, dim = x.shape
        
        q = self.query(x).view(batch_size, num_heads, seq_len, dim // num_heads)
        k = self.key(x).view(batch_size, num_heads, seq_len, dim // num_heads)
        v = self.value(x).view(batch_size, num_heads, seq_len, dim // num_heads)

        attention_weights = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.embed_dim)
        attention_weights = attention_weights.softmax(dim=-1)
        attention_weights = self.dropout(attention_weights)

        output = torch.matmul(attention_weights, v).view(batch_size, num_heads * seq_len, dim)
        
        return output

class Model(torch.nn.Module):
    def __init__(self, embed_dim=16, num_heads=8):
        super().__init__()

        self.attn = SelfAttention(embed_dim, num_heads=num_heads)

    def forward(self, x):
        out = self.attn(x)
        return out

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
