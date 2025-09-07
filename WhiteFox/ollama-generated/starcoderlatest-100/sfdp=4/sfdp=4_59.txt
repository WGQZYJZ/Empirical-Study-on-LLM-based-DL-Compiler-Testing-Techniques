
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head=8, d_model=512):
        super().__init__()
        self.n_head = n_head
        self.d_model = d_model
 
    def forward(self, query, key, value, attn_mask):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output
class PositionwiseFeedForward(torch.nn.Module):
    def __init__(self, d_ff=2048, dropout=0.1):
        super().__init__()
        self.w_1 = torch.nn.Linear(d_model, d_ff)
        self.w_2 = torch.nn.Linear(d_ff, d_model)
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, x):
        output  = self.w_2(torch.relu(self.w_1(x)))  # Apply linear transformation
        output += self.dropout(output)  # Dropout operation
        return output
class EncoderLayer(torch.nn.Module):
    def __init__(self, n_head=8, d_model=512, d_ff=2048, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(n_head, d_model)
        self.norm_1 = torch.nn.LayerNorm(d_model)
        self.positionwise_feed_forward = PositionwiseFeedForward(d_ff, dropout)
        self.norm_2 = torch.nn.LayerNorm(d_model)
 
    def forward(self, x):
        output  = self.norm_1(x + self.self_attn(x, x, x, attn_mask=None))  # Apply multi-head attention with query, key and value
        output  = self.norm_2(output + self.positionwise_feed_forward(output))  # Apply linear transformation after the multi-head attention
        return output
class Encoder(torch.nn.Module):
    def __init__(self, n_layer=6, n_head=8, d_model=512, d_ff=2048, dropout=0.1):
        super().__init__()
        self.layers = torch.nn.ModuleList()
        for _ in range(n_layer):
            self.layers.append(EncoderLayer(n_head, d_model, d_ff, dropout))
 
    def forward(self, x):
        output  = x
        for layer in self.layers:
            output  = layer(output)  # Apply all the layers to generate outputs from the input tensor
        return output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = Encoder(n_layer=6, n_head=8, d_model=512, d_ff=2048, dropout=0.1)
 
    def forward(self, x):
        output  = self.encoder(x)
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
