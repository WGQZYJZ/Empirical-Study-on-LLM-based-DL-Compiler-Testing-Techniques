
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale = 1.0):
        super().__init__()
 
        self.inv_scale = torch.full((3,), fill_value=inv_scale)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale**0.5 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
 
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = ScaledDotProductAttention()
 
# Inputs to the model (query, key and value tensors)
query = torch.randn((3200, 64)) # query tensor with shape [N x H] where N is batch size, H is dimension of query vector 
key = torch.randn(65538, 64) # key tensor with shape [M x H] where M is batch size or number of keys to be used for attention, H is the dimension of each key/query vector in the input sequence
value = torch.randn((3200, 64)) # value tensor with shape [N x H] where N is batch size and H is dimension of vector representing one token in sequence
 
# Running model
output1 = m(query, key, value)

