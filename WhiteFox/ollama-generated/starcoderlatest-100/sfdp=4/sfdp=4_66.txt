
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(10, 128)
        self.k = torch.nn.Linear(256, 32)
 
    def forward(self, q, k):
        attn_weight = torch.softmax((self.q @ self.k.transpose(-2, -1)) / math.sqrt(self.q.size(-1)), dim=-1) # (batch_size, num_heads, seq_len, input_dim // head_dim)
        output = attn_weight @ v  # (batch_size, num_heads, query_length, value_length)
        return output
# Inputs to the model
q = torch.randn(1, 8, 256).permute((0, 3, 1, 2))
k = torch.randn(1, 8, 4096).permute((0, 2, 3, 1))
attn_mask = torch.nn.functional.one_hot(torch.tensor([[1, 1, 1, 1, 1], [0, 0, 0, 0, 0]])).permute((1, 2, 0, 3)).unsqueeze(dim=0) # (batch_size, num_heads, seq_len, input_length)
