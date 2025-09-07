
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1, x2):
        v1 = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = torch.eye(v1.shape[-2], device=v1.device).unsqueeze(0).repeat(v1.shape[0], 1, 1, v1.shape[-2]) * -9e9 # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(v1 + attn_mask, dim=-1) # Apply softmax to the result
        output = (attn_weight @ x2).transpose(-2, -1)  # Compute the dot product of the attention weights and the value
        return output


# Inputs to the model
x1 = torch.randn(16, 3, 16, 16)
x2 = torch.randn(16, 8, 16, 16)
