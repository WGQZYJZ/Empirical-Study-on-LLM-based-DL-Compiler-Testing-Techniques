
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Linear(10, 5) # Projection layer for query with dimension 10 to output dimension 5
        self.attn_k = torch.nn.Linear(10, 5) # Projection layer for key with dimension 10 to output dimension 5
        self.attn_v = torch.nn.Linear(10, 256) # Projection layer for value with dimension 10 to output dimension 256
    def forward(self, x1, x2):
        attn_q = self.attn_q(x1).unsqueeze(-2) # The attn_q has shape [batch_size, seq_len, num_heads, head_dim] and will be repeated along the time dimension for each query in each step
        attn_k = self.attn_k(x2).unsqueeze(-3) # The attn_q has shape [batch_size, seq_len, num_heads, head_dim] and will be repeated along the time dimension for each key in each step
        qk = torch.einsum("bqhd,bkhd->bhqk", attn_q, attn_k) # The einsum operation computes the dot product between the two tensors at each step
        v = self.attn_v(x2).unsqueeze(-3) # Shape of query and key tensor for each step will be  [batch_size, seq_len, num_heads, head_dim] and will be repeated along the time dimension for each value in each step
        output = torch.einsum("bhqk,bkhd->bqhd", qk, v) # The einsum operation computes the dot product between the two tensors at each step
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048, 5)
x2 = torch.randn(32, 10, 64, 64)
