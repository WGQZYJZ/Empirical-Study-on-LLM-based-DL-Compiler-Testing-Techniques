
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 8)
        self.key = torch.nn.Linear(12, 16)
        self.value = torch.nn.Linear(5, 32)
 
    def forward(self, q1, k1):
        attn_weights = self._compute_scaled_dot_product_attention(q1, k1) # Compute scaled dot-product attention
        attn_weights += 0.5   # Add the attention mask to the scaled dot product
        attn_weights = torch.softmax(attn_weights, dim=-1) # Apply softmax on the result of softmax scaled dot-product attention
        return attn_weights @ self.value
 
 
def _compute_scaled_dot_product_attention(q1, k1):
    