
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product_attention = ScaledDotProductAttention()

    def forward(self, query, value, inv_scale):
        attention_output = self.scaled_dot_product_attention(query, value, inv_scale)
        return attention_output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 8)
key = torch.randn(16, 8)
inv_scale = math.sqrt(2 * 8) # (dimension of key/query vectors)**0.5
x = torch.randn(16, 8)
