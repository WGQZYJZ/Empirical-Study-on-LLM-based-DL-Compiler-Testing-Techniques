
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (math.sqrt(float(key.size()[-1])) * math.sqrt(float(value.size()[-1])))
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Inputs to the model
query  = torch.randn(1, 8, 64, 64)
key    = torch.randn(8, 16, 32, 32)
value  = torch.randn(16, 16, 32, 32)
