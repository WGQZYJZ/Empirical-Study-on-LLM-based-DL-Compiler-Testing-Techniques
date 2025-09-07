
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.k_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key):
        qv = self.q_conv(query) @ self.k_conv(key).transpose(-2, -1) # Compute the dot product of the queries and keys, and scale it
        attn_mask  = torch.ones((1, 8, 64, 64), device=qv.device)
        qv = qv + attn_mask
        attn_weight = torch.softmax(qv, dim=-1) # Apply softmax to the result
        output = torch.matmul(attn_weight, key) @ self.k_conv(key).transpose(-2, -1)  # Compute the dot product of the attention weights and the values
        return output

# Inputs to the model
q1 = torch.randn(2, 3, 64, 64)
k1 = torch.randn(2, 8, 64, 64)
