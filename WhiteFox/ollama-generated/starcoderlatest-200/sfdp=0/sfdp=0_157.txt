
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 2 ** 0.5
 
    def forward(self, query, key, value):
        # Compute scaled dot product attention using torch.matmul()
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.scale
 
        # Compute softmax on the scaled dot product 
        attention_weights = F.softmax(scaled_dot_product, dim=-1)
 
        # Context vector is the weighted sum of the value tensor
        context = attention_weights.matmul(value)
 
        return context, attention_weights


# Initializing the model
a = Attention()
 
# Inputs to the model
q  = torch.randn(256, 1024) # query tensor (batch size, dimension of embedding vector in hidden states of all heads at this layer)
k = torch.randn(256, 768) # key tensor (batch size, sequence length, dimension of embedding vector in hidden states of all heads at this layer)
v = torch.randn(256, 768) # value tensor (batch size, sequence length, dimension of embedding vector in hidden states of all heads at this layer)
__output__, __attention_weights__ = a(q, k, v)

 