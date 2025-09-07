
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(256, 8)
 
    def forward(self, x1, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (1 / math.sqrt(256))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
query = torch.randn(1, 256, 64, 64)
key   = torch.randn(1, 256, 64, 64)
value = torch.randn(1, 256, 64, 64)
