
class Attention(torch.nn.Module):
    def __init__(self, query_dim, key_dim, dim, dropout_p=0.5, use_bias=False):
        super().__init__()

        self.query = torch.nn.Linear(query_dim, dim, bias=use_bias)  # Query (hidden -> intermediate/output dims)
        self.key = torch.nn.Linear(key_dim, dim, bias=use_bias)  # Key (hidden -> intermediate/output dims)
        self.value = torch.nn.Linear(query_dim, dim, bias=use_bias)  # Value (hidden -> intermediate/output dims)

        self.dropout_p = dropout_p

    def forward(self, query, key):
        bs, c, h, w = query.shape
        q = self.query(query).view(bs, -1, c)  # Flatten to [bs*c, h*w] and multiply by linear projection layer

        k = self.key(key).view(bs, -1, c)  # Flatten to [bs*c, h*w] and multiply by linear projection layer
        v = self.value(key).view(bs, -1, c)  # Flatten to [bs*c, h*w] and multiply by linear projection layer

        qk = torch.matmul(q, k)  # Compute the dot product of the query and key tensors
        scaled_qk = qk / (math.sqrt(dim) * math.sqrt(q.size(-1)))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output

        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
        return output.view(bs, -1, h, w)


class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, query_dim, key_dim, dim, dropout_p=0.5, use_bias=False):
        super().__init__()

        self.attention = Attention(query_dim, key_dim, dim, dropout_p, use_bias)  # Apply attention
        self.layernorm1 = torch.nn.LayerNorm((query_dim + dim))  # Layer normalization applied to all elements of the output
        self.dense = torch.nn.Linear(dim, query_dim, bias=use_bias)  # Dense layer applied after the attention and layer norms
        self.layernorm2 = torch.nn.LayerNorm((query_dim + dim))  # Layer normalization applied to all elements of the output

    def forward(self, x):
        h = self.attention(x, x)  # Apply attention on all elements of the input tensor
        h = self.dense(torch.cat([x, h], -1))  # Dense layer
        return self.layernorm2(h + x)


class TransformerEncoder(torch.nn.Module):
    def __init__(self, n_layers=6, query_dim=3072, key_dim=3072, dim=512, dropout_p=0.5, use_bias=False):
        super().__init__()

        self.encoder = torch.nn.ModuleList([TransformerEncoderLayer(query_dim, key_dim, dim, dropout_p, use_bias)
                                            for _ in range(n_layers)])  # Transformer encoder layers
        self.dropout1 = torch.nn.Dropout2d(0.3)
        self.dropout2 = torch.nn.Dropout(0.4)

    def forward(self, x):
        h = x
        for layer in self.encoder:
            h = layer(h)  # Apply the Transformer encoder layers

        return self.dropout1(h) + self.dropout2(x)


class Model(torch.nn.Module):
    def __init__(self, n_layers=6, query_dim=3072, key_dim=3072, dim=512, dropout_p=0.5, use_bias=False):
        super().__init__()

        self.encoder = TransformerEncoder(n_layers, query_dim, key_dim, dim, dropout_p, use_bias)  # Transformer encoder layer
        self.linear = torch.nn.Linear(query_dim, 3072, bias=use_bias)  # Linear projection layer
        self.dropout1 = torch.nn.Dropout2d(0.4)
        self.dropout2 = torch.nn.Dropout(0.5)

    def forward(self, x):
        h = self.encoder(x)  # Apply the Transformer encoder layer

        h = self.linear(h)  # Linear projection to convert all elements of the output into a vector representation
        h = h.unsqueeze(-1)  # Add an extra dimension as last element in output tensor
        return self.dropout1(h) + self.dropout2(x)


class MultiheadSelfAttentionEncoderLayer(torch.nn.Module):
    def __init__(self, query_dim=3072, key_dim=3072, dim=512, n_heads=4, dropout_p=0000000000)
def main():
#    import matplotlib