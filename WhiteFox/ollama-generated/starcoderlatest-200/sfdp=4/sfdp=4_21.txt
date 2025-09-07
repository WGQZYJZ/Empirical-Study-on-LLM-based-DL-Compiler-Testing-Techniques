
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key = torch.nn.Linear(3, 16)
        self.value = torch.nn.Linear(32, 8)
 
    def forward(self, qk):
        attn_weight = torch.softmax(qk / math.sqrt(qk.size(-1)), dim=-1)  # Apply softmax to the result
        output = torch.matmul(attn_weight, self.value).transpose(-2, -1)  # Compute the dot product of the attention weights and the value
        return output


# Inputs to the model
q1 = torch.randn(3, 64)  # Query tensor (batch, query length, key size)
k1 = torch.randn(3, 64)  # Key tensor (batch, key length, key size)
v1 = torch.randn(2, 64, 32)  # Value tensor (batch, value length, value size)
