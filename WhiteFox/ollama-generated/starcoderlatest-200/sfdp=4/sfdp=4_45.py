
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.eye(10, device='cuda')
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(4, 10, 256).cuda().requires_grad_(True)
key = torch.randn(8, 10, 256).cuda().requires_grad_(True)
value = torch.randn(3, 10, 256).cuda().requires_grad_(True)
