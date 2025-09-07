
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, d_k: int = 32) -> None:
        super().__init__()
        self.d_k = d_k

    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.d_k)
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = attention_weights.matmul(value)
        return output


class Model(torch.nn.Module):
    def __init__(self, d_k: int = 32) -> None:
        super().__init__()
        self.attention = ScaledDotProductAttention(d_k=d_k)

    def forward(self, query, key, value):
        output = self.attention(query, key, value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(256, 32, 56, 56)
x2 = torch.randn(256, 16, 48, 48)
x3 = torch.randn(256, 32, 24, 24)
