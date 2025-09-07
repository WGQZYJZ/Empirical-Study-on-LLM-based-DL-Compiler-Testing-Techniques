
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm((3, 64, 64))
 
    def forward(self, query, key):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(64 * 64 * 1)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return self.layer_norm(output)


# Inputs to the model
query = torch.randn(1, 8, 3, 64, 64)
key = torch.randn(1, 8, 3, 64, 64)
