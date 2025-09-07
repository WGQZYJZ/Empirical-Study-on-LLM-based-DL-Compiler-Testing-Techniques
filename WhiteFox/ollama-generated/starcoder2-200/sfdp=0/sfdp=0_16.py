
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._scale = torch.tensor(100)
 
    def forward(self, query, key, value): 
        scaled_dot_product  = query @ key.transpose(-2, -1) / math.sqrt(_scale)
        attention_weights  = scaled_dot_product.softmax(dim=-1) # Calculate the softmax of the dot product
        output  = attention_weights @ value # Compute a weighted sum with the given value tensor
        return output
