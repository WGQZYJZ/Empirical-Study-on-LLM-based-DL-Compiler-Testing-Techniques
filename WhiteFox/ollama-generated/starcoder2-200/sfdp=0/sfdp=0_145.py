class DotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=None):
        super().__init__()
        self.inv_scale = 1 / (64 if inv_scale is None else inv_scale)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) * self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights @ value
        return output

model = DotProductAttention()
