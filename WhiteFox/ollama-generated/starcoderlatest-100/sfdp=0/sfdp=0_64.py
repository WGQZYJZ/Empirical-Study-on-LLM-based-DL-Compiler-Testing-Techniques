
class MultiheadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.embed_dim = embed_dim
        self.attention_weights = torch.nn.Parameter(
            torch.zeros((1, 1, 32, 512)), requires_grad=False)
 
    def forward(self, qkv):
        qk = qkv.chunk(2, dim=-1)
        query = qk[0]
        key = qk[1]
 
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(
            self.embed_dim)  # Dot product between two vectors, then scale the dot product by the square root of the dimension of the vectors
        attention_weights = scaled_dot_product.softmax(dim=-1)
 
        output = torch.matmul(attention_weights, qk[2])
        return output
class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.multihead_attention = MultiheadAttention(embed_dim=embed_dim, num_heads=num_heads)
 
        self.linear1 = torch.nn.Linear(in_features=embed_dim * 32, out_features=embed_dim)
        self.linear2 = torch.nn.Linear(in_features=embed_dim, out_features=embed_dim)
 
    def forward(self, x):
        # Multihead attention block
        qkv = torch.cat([
            self.multihead_attention(x),
            self.multihead_attention(x.permute(0, 2, 3, 1)),
            self.multihead_attention(x.permute(0, 3, 1, 2))
        ], dim=-1)
 
        # MLP blocks with Relu activation functions
        y = torch.relu(self.linear1(qkv))
        y = torch.relu(self.linear2(y))
 
        # Fused add and then element-wise product
        return self.multihead_attention(x + y)
class TransformerEncoder(torch.nn.Module):
    def __init__(self, num_layers, embed_dim, num_heads):
        super().__init__()
        layer = TransformerEncoderLayer(embed_dim=embed_dim, num_heads=num_heads)
        self.layer = torch.nn.ModuleList([copy.deepcopy(layer) for _ in range(num_layers)])
 
    def forward(self, x):
        output = x
        for layer_block in self.layer:
            output = layer_block(output)
 
        return output
class Model(torch.nn.Module):
    def __init__(self, num_layers=2, embed_dim=512, num_heads=8):
        super().__init__()
        self.encoder = TransformerEncoder(num_layers=num_layers, embed_dim=embed_dim, num_heads=num_heads)
 
    def forward(self, x):
        output = self.encoder(x)
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
