
class DotProductAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.scale = 1 / math.sqrt(dim)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) * self.scale 
        attention_weights = scaled_dot_product.softmax(dim=-1)
        return  attention_weights.matmul(value), attention_weights

model  = DotProductAttention(768)

