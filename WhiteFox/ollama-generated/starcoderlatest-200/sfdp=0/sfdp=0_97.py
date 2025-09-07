
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 256)
 
    def forward(self, query, key, value, mask=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(8 * 256)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = self.attention(attention_weights, value, value)[0]
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 8, 512, 64)
key = torch.randn(2, 8, 512, 64)
value = torch.randn(2, 8, 512, 64)
mask = None
