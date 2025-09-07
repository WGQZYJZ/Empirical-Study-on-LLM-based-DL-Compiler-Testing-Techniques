
class Model(torch.nn.Module):
    def __init__(self, num_attn_heads, hidden_dim, max_len=128, dropout_p=0):
        super().__init__()
 
        self.conv1 = torch.nn.Conv2d(3, 64, 1)
        self.conv2 = torch.nn.Conv2d(64, 128, 1)
 
        self.self_attn = torch.nn.MultiheadAttention(num_attn_heads, hidden_dim)
        self.linear1 = torch.nn.Linear(hidden_dim, max_len * hidden_dim)
        self.layer_norm = torch.nn.LayerNorm(max_len * hidden_dim)
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, x):
        # (batch, channel, height, width)
        h = self.conv1(x)
        h = F.relu(h)
 
        h = self.conv2(h)
        h = F.relu(h)
 
        q  = self.self_attn(
            h, h, h, mask=None, key_padding_mask=None, need_weights=True)
        q = self.dropout(q, training=training)
 
        # Scale and shift the input data according to the attention weights.
        # The attention mechanism expects the shift to be equal to `query_len` times `key_len`.
        query_len = x.size(-2)  # (batch,)
        key_len = h.size(-2)  # (batch,)
 
        q = q * math.sqrt(float(query_len))
        q += math.exp(q)  # (batch, query_len, hidden_dim)
        k = h * math.sqrt(float(key_len))
        k += math.exp(k)  # (batch, key_len, hidden_dim)
 
        # Perform a linear transformation of the output to get back to the original shape.
        x = torch.matmul(q, k).transpose(-2, -1)
        x = self.layer_norm(x + h)
        return x


# Initializing the model
m = Model()

