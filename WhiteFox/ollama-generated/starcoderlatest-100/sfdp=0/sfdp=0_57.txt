
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(8, 8)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()
# Inputs to the model
query = torch.randn(8, 64, 8, 64)
key   = torch.randn(8, 64, 8, 64)
value = torch.randn(8, 64, 128, 128)
