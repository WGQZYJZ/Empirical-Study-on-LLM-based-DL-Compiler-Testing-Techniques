
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(dim_q=32, dim_kv=16)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / 8
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(16, 32, 128, 128)
key = torch.randn(16, 32, 56, 56)
value = torch.randn(16, 32, 56, 56)
