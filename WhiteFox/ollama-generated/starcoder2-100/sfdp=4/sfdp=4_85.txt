
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
 
        # Compute the dot product of the query and key tensors
        qk = torch.bmm(query, key.transpose(-2,-1)) / math.sqrt(query.size(-1))
 
        # Add the attention mask to the scaled dot product
        if not attn_mask is None:
            qk  += attn_mask
        attn_weight  = torch.softmax(qk)
 
        output = torch.bmm(attn_weight, value)
 
return output

