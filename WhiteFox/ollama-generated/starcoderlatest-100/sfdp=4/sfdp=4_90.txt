
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(8, 64)
 
    def forward(self, q1, k1, v1):
        bsz = q1.size(0) # Get the batch size
        qk  = query @ key.transpose(-2, -1) / math.sqrt(q1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = (attn_mask_values < unk).unsqueeze(dim=1).expand(bsz, 16, q1.size(-2), q1.size(-3)) * -1e8
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Apply softmax to the result
        output  = attn_weight @ v1 # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(1, 16, 8, 64)
k1 = torch.randn(1, 32, 8, 64)
v1 = torch.randn(1, 32, 8, 64)
attn_mask_values = torch.ones((1, 32, 8, 64)) * -1e5
