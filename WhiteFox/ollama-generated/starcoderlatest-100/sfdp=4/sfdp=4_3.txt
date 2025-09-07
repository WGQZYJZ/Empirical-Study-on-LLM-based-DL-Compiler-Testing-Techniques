
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_module = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, attn_mask):
        qk = self.attention_module(query, key, key, need_weights=False)  # Compute the attention weights
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Multiply the scaled dot-product attention weights with the value tensor
        return output
# Initializing the model
m = Model()
# Inputs to the model
query = torch.randn(2, 5, 1024)
key = torch.randn(3, 5, 1024)
value = torch.randn(2, 5, 768)
attn_mask = torch.eye(1, dtype=torch.float).unsqueeze(0)  # Create an attention mask to prevent attending to certain positions
