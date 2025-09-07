
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        qk  = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output  = attn_weight @ value # Compute the dot product of the attention weights and the value tensor
        return output

# Initializing the model
m  = Model()
 
# Inputs to the model
key  = torch.randn(4, 256, 783)
query1= torch.randn(4, 256, 783)
query2 = query1 + (torch.rand_like(key).uniform_() - 0.5) * 5 # Add a random noise to the query tensor in order to obtain a new query tensor with different output
attn_mask = torch.ones((4, 783), device='cuda', requires_grad=False)
 
# Initializing the mask attn_mask with True values
attn_mask1 = attn_mask
attn_mask2 = attn_mask + (torch.rand(4*256*783).normal_(0, 0.05)) * 20 # Add a random noise to the attention mask tensor in order to obtain a new attention mask with different output
 
# Generating an input for the first case
x1 = (query1, key, attn_mask)
__output__1 = m(*x1) # Generate an output for the first case

# Generating an input for the second case
x2  = (query2, key, attn_mask2)
__output__2 = m(*x2) # Generate an output for the second case
 
