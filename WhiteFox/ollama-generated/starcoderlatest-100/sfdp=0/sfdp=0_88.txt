
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(num_heads=8, embed_dim=1024)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, 8, 512, 64)
key = torch.randn(1, 8, 512, 64)
value = torch.randn(1, 8, 512, 64)
