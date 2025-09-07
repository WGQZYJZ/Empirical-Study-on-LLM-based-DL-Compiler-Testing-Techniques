
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=128):
        super().__init__()
        self.dim = dim
 
    def forward(self, q, k, v):
        # This method computes scaled dot product attention using a fixed scale `inv_scale` to stabilize gradients.
        # Since the dimensions of input tensor cannot exceed `MAX_DIM`, it is used as a multiplier for the square root of `inv_scale`.
        
        inv_scale = 1 / (q.shape[-2] ** 0.5) 
        q = torch.einsum('bnld, bndi -> bnij', [q, k]) * inv_scale
        attention_weights = torch.softmax(q, dim=-1)
        output = attention_weights.matmul(v)

        return output

class MultiHeadDotProductAttention(torch.nn.Module):
    def __init__(self, num_heads=8, dim=128):
        super().__init__()
        self.num_heads = num_heads
        self.dim = dim
        self.head_dim = dim // num_heads
 
        self.query_layer = torch.nn.Linear(dim, dim)
        self.key_layer = torch.nn.Linear(dim, dim)
        self.value_layer = torch.nn.Linear(dim, dim)

        self.fc = torch.nn.Linear(self.num_heads * self.head_dim, dim)
 
    def forward(self, q, k, v):
        batch_size = q.shape[0]
 
        # Project and split query and key vectors into multiple heads.
        num_heads = q.shape[-2]
        split_q = torch.split(q, self.head_dim, dim=-1)
        split_k = torch.split(k, self.head_dim, dim=-1)
        split_v = torch.split(v, self.head_dim, dim=-1)
 
        q = [self.query_layer(x).view(batch_size, -1) for x in split_q]  # (batch_size, num_heads * head_dim)
        k = [self.key_layer(x).view(batch_size, -1) for x in split_k]  # (batch_size, num_heads * head_dim)
        v = [self.value_layer(x).view(batch_size, -1) for x in split_v]  # (batch_size, num_heads * head_dim)
 
        q = torch.cat(q, dim=-2)  # (batch_size, ..., num_heads * head_dim)
        k = torch.cat(k, dim=-2)  # (batch_size, ..., num_heads * head_dim)
        v = torch.cat(v, dim=-2)  # (batch_size, ..., num_heads * head_dim)
 
        scaled_dot_product = torch.einsum('bnij, bnj -> bnij', q, k) / (self.head_dim ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
 
        # Combine heads and scale the result to obtain a single vector per head.
        combined_output = torch.cat([x.view(batch_size, -1, self.num_heads, self.head_dim) for x in split_v], dim=-2).mean(dim=-2)  # (batch_size, ..., num_heads * head_dim)
        combined_output = torch.cat([combined_output[:, :, i] for i in range(self.num_heads)], dim=2).view(batch_size, -1)
 
        return output
 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = torch.nn.Embedding(50000, 64, padding_idx=0) # word embedding dimension 64

        self.position_encoding = PositionalEncoding(dim=128)
 
        self.transformer_layer = torch.nn.TransformerEncoderLayer(d_model=64, nhead=8)
        self.transformer_encoder = torch.nn.TransformerEncoder(self.transformer_layer, 5)

        self.last_layer = torch.nn.Linear(128 * 8, 50000)

    def forward(self, x):
        embedding = self.encoder(x)
        encoded = self.position_encoding(embedding).permute(1,0,2) # (bsz, emb_dim, seq_len)
 
        output = self.transformer_encoder(encoded)

        return self.last_layer(output[:, :, -1])
# Inputs to the model
x1 = torch.randint(low=0, high=50000, size=(32, 2)) # (bsz, max_len)
