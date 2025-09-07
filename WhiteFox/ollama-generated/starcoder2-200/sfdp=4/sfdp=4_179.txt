
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None): 
        scale = math.sqrt(query.size(-1)) # Compute the square root of the dimensionality of a tensor
        qk  = query @ key.transpose(-2, -1) / scale # Compute the dot product of the query and key tensors, and divide it by sqrt(d_q)
        qk += attn_mask if attn_mask is not None else torch.zeros(qk.size()).type(query.dtype).to(query.device) 
        attn_weights  = torch.softmax(qk, dim=-1) # Apply the softmax function to the dot product
        return (attn_weights @ value), attn_weights


class TransformerModel(torch.nn.Module):
    def __init__(self):
         super().__init__()
         self.net = torch.nn.Sequential(...)
 
    def forward(self, inputs1): 
        outs  = self.net(inputs1)
        return outs


# Initializing the model
m  = TransformerModel()
 
# Input to the model
x2  = torch.randn(640, 80, 768)

 # Initializing the attention module
attn_module = SelfAttention()
 
# Inputs for the transformer
inputs1  = x2[:, None]
inputs2  = attn_module(query=inputs1, key=inputs1, value=x2, attn_mask=None)[0].permute([0, 3, 2])

 