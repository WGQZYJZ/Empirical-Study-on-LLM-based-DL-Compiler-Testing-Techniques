
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=128, num_heads=8)
 
    def forward(self, qk):
        qk  = torch.matmul(qk, qk.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v1  = self.attention(qkv1)[0] # Get the output tensor with shape [batch_size, seq_len_k, embed_dim], where embed_dim is equal to self-attention embedding size
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4  + 1
        v6  = v2  * v5
        return v6


# Inputs to the model
qk = torch.randn(2, 8, 300, 768)
