
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.Linear(1024, 8)
        self.mlp   = torch.nn.Linear(1024, 8)
 
    def forward(self, x1, x2):
        vq  = torch.cat([x1, x2], dim=-1)  # Concatenate the input tensors together
        attn_mask = self.compute_attn_mask(vq)  # Compute the attention mask
        attn_weight = self.softmax(self.attention(vq, x2), dim=-1) # Apply softmax to the result
        output  = attn_weight @ self.mlp(self.mlp(x2)) # Compute the dot product of the attention weights and the value
        return output
 
    def compute_attn_mask(self, vq):
        attn_mask = torch.zeros(vq.shape[:-1] + (8,), device=vq.device) # Create the zero-filled attention mask
        attn_mask[..., 0::2] = 1 # Set the diagonal of the attention mask to 1
        return attn_mask
 
    def attention(self, vq, x):
        output  = torch.matmul(x, vq.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        logit   = F.log_softmax(output, dim=-1)  # Apply softmax to the result
        attn    = torch.bmm(logit, x.transpose(-2, -1)) # Compute the dot product of the attention weights and the value
        return attn
 
