class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        inv_scale  = ((query.size(-1)) ** (-0.5)).item()
        scaled_dot_product  = torch.matmul(query / inv_scale, key.transpose(-2, -1) / inv_scale) # Scaled dot product attention with scaling factor of sqrt(d_k), where d_k is the dimensionality of each vector (typically ~ 64)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value / inv_scale) # Output is a weighted sum of value vectors with scaled dot product attention weights, with scaling factor sqrt(d_k)
        return output
