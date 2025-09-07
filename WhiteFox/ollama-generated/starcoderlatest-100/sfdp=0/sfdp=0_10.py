
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output
# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 8, 50, 64)
key = torch.randn(2, 8, 50, 64)
value = torch.randn(2, 8, 50, 128)
inv_scale = 1e-4
