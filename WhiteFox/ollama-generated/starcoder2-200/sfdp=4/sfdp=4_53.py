
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        s  = torch.einsum("q, k -> qk", [q1, k1]) / math.sqrt(math.prod(k1.shape[-2:], dtype=float)) 
        s += attn_mask # Add the attention mask to the scaled dot product
        attn_weights  = torch.softmax(s, dim=-1) # Apply softmax to the result
        output = torch.einsum("qk, v -> qv", [attn_weights, v1]) # Compute the dot product of the attention weights and the value
        return output


# Initializing the model:
m  = Model()
 
# Inputs for the model (tensors)
q1   = torch.randn(32, 80, 576)# Input query tensor with shape [batch_size, num_queries, hidden_size]
k1  = torch.randn(32, 576, 4096) # Input key tensor with shape [batch_size, num_keys, hidden_size]
v1   = torch.randn(32, 80, 4096)# Input value tensor with shape [batch_size, num_keys, hidden_size]
 
attn_mask = torch.zeros((q1.shape[1], k1.shape[-1]), device="cpu") # Construct the attention mask to be used in this model (attention mask shape is [batch_size x key_sequence_length])

# Inputs for the model (tensors)
k1   = torch.randn(32, 576, 4096)# Input key tensor with shape [batch_size, num_keys, hidden_size]
 
attn_mask = torch.zeros((q1.shape[1], k1.shape[-1]), device="cpu") # Construct the attention mask to be used in this model (attention mask shape is [batch_size x key_sequence_length])

