
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(
            torch.randn((2, 3, 1, 64, 64)), requires_grad=False)
        self.key = torch.nn.Parameter(
            torch.randn((2, 3, 64, 64)), requires_grad=False)
 
    def forward(self, x1, x2):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + torch.nn.functional.multi_head_attention_forward_input_tensor(q1, v2, k3, attn_mask=attn_mask)[0] # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ self.value # Compute the dot product of the attention weights and the value
        return output

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
attn_mask = torch.ones_like(q1)
