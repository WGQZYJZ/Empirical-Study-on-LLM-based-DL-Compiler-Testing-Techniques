
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        attn = torch.einsum('bmn,bmj->bjm', 
                             [x1, x2], # query
                             [x1, x2]) + torch.ones([attn_mask.size()[:3] + 
                                           (attn_mask.size(-1), 
                                            x1.shape[-2] * x1.shape[-1]), attn_weight.size(-2)])
        attn = softmax(attn) # Attention weights as the softmax of the dot product 
        attn = torch.dropout(attn, dropout_p=0.5) # Apply dropout to the attention weights 
        v  = torch.einsum('bnl->bl', [x1, x2]) + attn @ value  # Compute the result as a weighted sum
        return v

# Initializing the model