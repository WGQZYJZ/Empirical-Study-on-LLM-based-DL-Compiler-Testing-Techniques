
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.norm = torch.nn.LayerNorm([64])
 
    def forward(self, query, key):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size()[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return self.norm(output + query)


# Initializing the model
m = Model()
q = torch.randn(2, 3, 64, 64)
k = torch.randn(1, 3, 64, 64)
v = torch.randn(1, 3, 64, 64)
