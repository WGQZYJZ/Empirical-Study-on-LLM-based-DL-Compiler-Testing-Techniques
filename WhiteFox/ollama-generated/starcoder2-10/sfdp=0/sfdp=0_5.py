
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        # Compute scaled dot product attention
        inv_scale = torch.sqrt(key.size(-1))  # Assuming square matrices of size (..., key_dim) and (..., value_dim)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        
        # Compute attention weights by applying softmax on the scaled dot product
        attention_weights = scaled_dot_product.softmax(dim=-1)
        
        # Compute output as a weighted sum of value vectors using attention weights
        output = torch.bmm(attention_weights, value)
    
        return output

m  = Model()

q  = torch.randn((32, 64))
k  = torch.randn((32, 512, 64)) # Assuming 512 x 64 matrix as the key vector in Scaled Dot-Product Attention (SDPA) mechanism for Transformer models
v  = torch.randn((32, 512, 64)) # Assuming 512 x 64 matrix as the value vector in SDPA mechanism for Transformer models

__output__  = m(q, k, v).shape

