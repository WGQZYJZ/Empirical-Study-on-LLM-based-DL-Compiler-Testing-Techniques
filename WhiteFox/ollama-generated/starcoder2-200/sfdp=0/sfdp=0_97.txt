
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.key  = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
 
    def forward(self, query):
        key  = self.key(query)
        value  = self.value(query)
        
        # scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        inv_scale = math.sqrt(query.shape[-1])
 
        query_expand = query.repeat([key.shape[0]] + [1] * (len(query.shape) - 1))
        scaled_dot_product  = torch.matmul(query_expand, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)

        output  = attention_weights.matmul(value)
        
        return output


# Initializing the model
m  = Attention(4)

