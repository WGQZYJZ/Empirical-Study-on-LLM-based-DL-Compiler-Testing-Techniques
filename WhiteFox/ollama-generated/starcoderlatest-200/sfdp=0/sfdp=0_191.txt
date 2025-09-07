
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=128, query_embed_dim=512, value_embed_dim=768, out_embed_dim=768):
        super().__init__()
        self.num_heads = num_heads
        self.key_layer  = torch.nn.Linear(query_embed_dim, query_embed_dim*num_heads)
        self.value_layer = torch.nn.Linear(value_embed_dim, value_embed_dim*num_heads)
        self.output_layer= torch.nn.Linear(query_embed_dim * num_heads, out_embed_dim)
    
    def forward(self, query, key, value):
        batch_size = query.shape[0]
        qkv = torch.cat([query, key, value], dim=-1)
        qkv = self.key_layer(qkv).reshape(batch_size, -1, 3 * self.num_heads)
        qkv = qkv.permute(2, 0, 1).contiguous().view(-1, 3 * self.num_heads, batch_size, query.shape[2])
        
        attention_weights = torch.matmul(qkv, torch.transpose(self.value_layer(qkv), -2, -1)).reshape(batch_size, -1, query.shape[2], 3 * self.num_heads)
        attention_weights = F.softmax(attention_weights, dim=-3).masked_fill(torch.arange(batch_size, device=device)[:, None] >= batch_size, -float("inf"))
        
        output = torch.matmul(attention_weights, value).reshape(batch_size, query.shape[1], self.num_heads * query.shape[2])
        return self.output_layer(output)


class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, embed_dim=768, num_heads=128):
        super().__init__()
        self.feed_forward = torch.nn.Sequential(
            torch.nn.Linear(embed_dim*4, 3 * embed_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(3 * embed_dim, embed_dim)
        )
        
        self.attention_layer = MultiHeadAttention(num_heads=num_heads)
    
    def forward(self, x):
        x = self.feed_forward(x) + x
        return self.attention_layer(x[:, :, :embed_dim], x[:, :, embed_dim:2*embed_dim], x[:, :, 2*embed_dim:])
class TransformerEncoder(torch.nn.Module):
    def __init__(self, num_layers=3, embed_dim=768, num_heads=128):
        super().__init__()
        self.layers = torch.nn.Sequential(*[TransformerEncoderLayer(embed_dim=embed_dim, num_heads=num_heads) for _ in range(num_layers)])
    
    def forward(self, x):
        return self.layers(x)


class Model():
    def __init__(self):
        super().__init__()
        encoder = TransformerEncoder()
        
        self.encoder = encoder

    def forward(self, x):
        h  = self.encoder(x)
        return h


# Inputs to the model
x1 = torch.randn(1024, 3, 64, 64).cuda()
