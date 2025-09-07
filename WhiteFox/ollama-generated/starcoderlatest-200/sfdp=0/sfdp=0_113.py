
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.sqrt(torch.tensor([0.5]))
 
    def forward(self, query, key, value):
        q_s, _ = query.shape # shape: (B, N, E) where B is batch size, N is length of the sequence and E is embedding dimension
 
        dim_head = self.scale * q_s # shape: (B, N, S) where B is batch size, N is length of the sequence and S is number of heads
        
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / dim_head
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Inputs to the model
q  = torch.randn(1, 8, 64, 64) # shape: (B, N, E), where B is batch size and N is length of the sequence
k = torch.randn(1, 8, 64, 64) # shape: (B, N, E) where B is batch size and N is length of the sequence
v = torch.randn(1, 8, 64, 64) # shape: (B, N, E), where B is batch size and N is length of the sequence


# Attention layer
attention_layer = Attention()
 
# Forward pass to compute output
output = attention_layer(q, k, v)

 