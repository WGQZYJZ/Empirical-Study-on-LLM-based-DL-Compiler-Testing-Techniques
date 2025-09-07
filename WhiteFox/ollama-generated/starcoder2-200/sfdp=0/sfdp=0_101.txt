
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=20):
        super().__init__()
        self.inv_scale = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value) 
        return output


m  = ScaledDotProductAttention()

 # Inputs to the model