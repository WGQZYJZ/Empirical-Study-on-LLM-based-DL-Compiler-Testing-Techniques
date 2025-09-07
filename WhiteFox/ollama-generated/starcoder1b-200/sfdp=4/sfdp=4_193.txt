
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn((10, 256), dtype=torch.float32)) # (batch_size, sequence_length)
        self.key   = torch.nn.Parameter(torch.randn((256, 128), dtype=torch.float32)) # (sequence_length, hidden_dim)
        self.value = torch.nn.Parameter(torch.randn((256, 512), dtype=torch.float32)) # (sequence_length, hidden_dim)
 
    def forward(self, x1):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        v = attn_weight @ self.value
        return v


# Initializing the model
m = Model()

