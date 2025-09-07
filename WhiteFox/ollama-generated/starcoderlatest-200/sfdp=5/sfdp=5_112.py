
class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, num_attention_heads, embedding_dim, ffn_embedding_dim, ffn_num_layers=1, dropout=0.1):
        super().__init__()
        
        self.self_attn = MultiheadAttention(
            num_attention_heads=num_attention_heads, 
            embedding_dim=embedding_dim, 
        )
        self.feedforward = nn.Sequential(
            nn.Linear(embedding_dim, ffn_embedding_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(ffn_embedding_dim, embedding_dim)
        )
    
    def forward(self, query, key, value): 
        attn = self.self_attn(query, key, value) # Apply multihead attention to the queries and keys
        ffn = self.feedforward(attn + query) # Apply feed-forward network (GELU activation) with dropout on the sum of the multihead attention output and the input tensor
        return ffn


class TransformerEncoder(torch.nn.Module):
    def __init__(self, num_layers, embedding_dim, num_attention_heads, ffn_embedding_dim, dropout=0.1):
        super().__init__()
        
        self.layers = nn.Sequential(*[TransformerEncoderLayer(
            num_attention_heads=num_attention_heads, 
            embedding_dim=embedding_dim, 
            ffn_embedding_dim=ffn_embedding_dim) for _ in range(num_layers)])
    
    def forward(self, x):
        x = self.layers(x) # Apply the TransformerEncoderLayer layer to all the input tensors (the output tensor of the last transformer encoder layer is the input tensor of the next one)
        return x


class Model(torch.nn.Module):
    def __init__(self, num_layers=4, embedding_dim=32, num_attention_heads=8, ffn_embedding_dim=64):
        super().__init__()
        
        self.encoder = TransformerEncoder(
            num_layers=num_layers, 
            embedding_dim=embedding_dim, 
            num_attention_heads=num_attention_heads,
            ffn_embedding_dim=ffn_embedding_dim)
    
    def forward(self, x):
        x = self.encoder(x) # Apply the TransformerEncoder to all the input tensors (the output tensor of the last transformer encoder layer is the input tensor of the next one)
        return x


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
