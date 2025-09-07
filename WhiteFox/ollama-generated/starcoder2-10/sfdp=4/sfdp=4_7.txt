
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale = torch.rsqrt(query.size(-1))
        dot  = query @ key.transpose(-2, -1) * scale # Compute the dot product of the query and key tensors; multiply the result by the square root of the dimension of the query tensor (assuming that each query vector is represented as a row of this matrix); note that this scaling factor will be used to re-normalize the dot products during softmax calculation.
        qk  = dot + attn_mask # Add the attention mask to the scaled dot product, which prevents attention to certain positions.
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result; the dimension for computing the softmax is the negative direction of the last two dimensions (i.e., -2 and -1).
        output  = attn_weight @ value 
        return output


# Initializing the model
am  = AttentionModel()
 
 
# Inputs to the model
q, k, v  = torch.randn(30, 64, 7), torch.randn(30, 8, 256), torch.randn(30, 8, 19)
 
__output__  = am(q, k, v)

