
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_k: int, num_heads: int, dropout_p: float = 0.1):
        super().__init__()
        self.d_k = d_k
        self.num_heads = num_heads
        assert d_k % num_heads == 0 # Make sure the depth is divisible by the number of heads
        self.depth = d_k // num_heads

        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.layer_norm = torch.nn.LayerNorm(d_k)

        self.scaling = (self.d_k ** -0.5)

    def split_heads(self, x: torch.Tensor):
        n, c = x.shape
        return torch.split(x, self.num_heads * self.depth, dim=1)

    def merge_heads(self, x: torch.Tensor):
        n, h, c = x.shape
        return torch.cat(torch.split(x, self.num_heads * self.depth, dim=1), dim=2).reshape((n, -1, c))

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        q = self.layer_norm(query)
        k = self.layer_norm(key)
        v = self.layer_norm(value)

        q, k, v = map(self.split_heads, (q, k, v))
        q *= self.scaling

        attention = torch.matmul(q, k.transpose(-2, -1))

        attention = attention / math.sqrt(self.d_k)
        attention = torch.nn.functional.softmax(attention, dim=-1)
        attention = self.dropout(attention)

        output = torch.matmul(attention, v)
        output = self.merge_heads(output)

        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        d_k  = 64 # Key dimension in multi-head attention mechanism
        num_heads = 8 # Number of heads in multi-head attention mechanism
        dropout_p = 0.1

        self.attention = MultiHeadAttention(d_k, num_heads, dropout_p)

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        return self.attention(q, k, v)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 32, 64) # Query tensor (batch size x heads x sequence length x head dimension)
x2 = torch.randn(1, 8, 32, 64) # Key tensor (batch size x heads x sequence length x head dimension)
x3 = torch.randn(1, 8, 32, 64) # Value tensor (batch size x heads x sequence length x head dimension)
