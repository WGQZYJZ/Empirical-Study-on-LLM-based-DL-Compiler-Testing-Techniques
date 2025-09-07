
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, temperature=1e-3):
        super().__init__()
        self.temperature = temperature
 
    def forward(self, query, key, value, attn_mask=None):
        # Compute the dot product of the query and key matrices
        energy  = torch.matmul(query, key) / math.sqrt(key.size(-1))
 
        if attn_mask is not None:
            # Add the mask to the scaled dot product matrix
            energy += attn_mask
        
        # Softmax over each row of the scaled dot product matrix
        attention = torch.softmax(energy / self.temperature, dim=-1)
        output  = torch.matmul(attention, value)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.zeros([432, 432], dtype=torch.bool).cuda()
        self.scaled_dot_product_attention = ScaledDotProductAttention(temperature=1e-3)

    def forward(self, query):
        # Initialize key and value matrices with the same shape as that of the query matrix
        key  = torch.zeros([432, 432], dtype=query.dtype).cuda()
        value  = torch.zeros_like(key)
 
        # Call the scaled dot product attention mechanism
        output  = self.scaled_dot_product_attention(query, key, value, attn_mask=self.attn_mask)
        return output


# Initializing the model
m  = Model()
 
# Input to the model (a torch.Tensor of shape [432 x 768])
query  = torch.randn(10000, 50).cuda()
 
