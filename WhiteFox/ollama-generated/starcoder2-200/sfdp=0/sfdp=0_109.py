
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query  = torch.nn.Linear(dim, dim)
        self.key  = torch.nn.Linear(dim, dim)
        self.value  = torch.nn.Linear(dim, dim)
 
        self.softmax  = torch.nn.Softmax(dim=-1)
 
    def forward(self, query_inputs):
        scaled_dot_product  = self._compute_scaled_dot_product(query_inputs)
        attention_weights  = self.softmax(scaled_dot_product)
        output  = attention_weights @ self.value(query_inputs).transpose(-2, -1)
 
        return output
 
    def _compute_scaled_dot_product(self, query):
        dim  = query.shape[-1]
        inv_scale  = torch.rsqrt(torch.tensor([dim]))
 
        key  = self.key(query)
        query  *= inv_scale
        key  += self.key(query).transpose(-2, -1)
 
        return torch.matmul(query / dim, key)


# Initializing the model with the appropriate input tensor size as an argument to the Attention module
attn = Attention(50)
input_tensor  = torch.randn(3, 50, 480).cuda()
 
__output__  = attn(input_tensor)

