
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)

    def forward(self, query, key, value, scaled_dot_product):
        v1 = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()
query = torch.randn(1, 32, 512, 64)
key   = torch.randn(1, 16, 512, 64)
value = torch.randn(1, 8, 1024, 64)
scaled_dot_product = query * key


# Inputs to the model
x1 = scaled_dot_product.softmax(-1)
output = m(query, key, value, x1)


