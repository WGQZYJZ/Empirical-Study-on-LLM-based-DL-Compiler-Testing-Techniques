
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(2048, 512) 
        self.key = torch.nn.Linear(2048, 512)
        self.value = torch.nn.Linear(2048, 512)

    def forward(self, x1, x2):
        query = self.query(x1).permute(0, 2, 3, 1) # (B, T_q, H, W) -> (B, H, W, T_k)
        key = self.key(x2).transpose(-2, -1) # (B, T_k, H, W) -> (B, H, W, T_k)
        value = self.value(x2) # (B, T_v, H, W) -> (B, H, W, T_v)
        qk = torch.matmul(query, key) # (B, N, 1, H) @ (B, H, N, 1) -> (B, N, N)
        attn_mask = -9e6 * (qk < 0) # (B, N, N) -> (B, N, N) -> (B, N, N)
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Compute the softmax of the scaled dot product of the query and key (plus an attention mask), followed by a dropout operation
        output = torch.matmul(attn_weight, value).permute(0, 3, 2, 1) # Compute the dot product of the dropout output and the value 
        return output
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
