
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        # Compute the dot product of the query and key tensors:
        qk  = torch.bmm(query, key.transpose(-2, -1))
 
        # Scale it by sqrt of the size of the last dimension of the query tensor.
        qk /= math.sqrt(query.size(-1))
 
        # Add an attention mask if one is given:
        if attn_mask != None:
            qk += attn_mask
 
        # Compute attention weights as softmax of the scaled dot product:
        attn_weight = torch.softmax(qk, dim=-1)
 
        # Compute weighted sum of value tensor using attention weights:
        output  = (attn_weight @ value).transpose(-2,-1)
        return output


# Initializing model
m  = SelfAttention()

# Inputs to the model