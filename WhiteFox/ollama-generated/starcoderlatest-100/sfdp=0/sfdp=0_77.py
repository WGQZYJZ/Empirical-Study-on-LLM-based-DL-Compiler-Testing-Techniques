
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(1, 8)
 
    def forward(self, x1, x2, query, key, value):
        attention_weights = self.attn(x1, x2, x2)[0]
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        return attention_weights

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 8, 10, 64)
key = torch.randn(1, 8, 20, 64)
value = torch.randn(1, 8, 30, 64)
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
