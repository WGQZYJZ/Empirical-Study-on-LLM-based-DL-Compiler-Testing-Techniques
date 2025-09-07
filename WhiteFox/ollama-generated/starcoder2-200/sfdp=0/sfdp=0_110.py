
class Attention(torch.nn.Module):
    def __init__(self, dim, inv_scale):
        super().__init__()
        self.key = torch.nn.Linear(dim, 1)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (inv_scale ** .5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

m = Attention(64, 0.7)

