
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads):
        super().__init__()
        self.num_attention_heads = num_attention_heads
 
    def forward(self, x1):
        # Initialize the model weights
        qk = torch.bmm(x1, x1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        attn_mask = (torch.tril(torch.ones(qk.size(-1), kq.size(-1)), 0) +
                     torch.triu(torch.ones(qk.size(-1), kq.size(-1)), -1)).bool() # Calculate the attention mask
        attn_mask = attn_mask.unsqueeze(0).unsqueeze(-2).unsqueeze(-3) # Pre-allocate the mask for use in the backward pass
        
        # Compute the scaled dot product of x and query, and scale it by sqrt(n), to get the scaled dot product
        v = torch.bmm(attn_weight.unsqueeze(1), x1)  # Compute the dot product of the attention weights and the value tensors
        attn_weights = torch.softmax(v, dim=-1) # Apply softmax on the weighted sum of the value tensors
        
        # Calculate the output weights, using the scaled dot products of query and key
        v = torch.bmm(attn_weights.unsqueeze(-2), attn_weights).squeeze(-3)  # Compute the output of a scaled dot product
        return x1 * v


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
