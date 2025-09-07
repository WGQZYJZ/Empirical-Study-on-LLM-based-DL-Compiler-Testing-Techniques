
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.norm = torch.nn.LayerNorm()
 
    def forward(self, query, key, value, mask=None, att_dropout=0.1):
        dim  = key.size(-2)
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(float(dim))
 
        if mask is not None:
            scaled_dot_product += (mask * -1e9).type_as(scaled_dot_product)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = self.norm(attention_weights.matmul(value))
 
        return output


# Initializing the model
sdpa = ScaledDotProductAttention()
 
