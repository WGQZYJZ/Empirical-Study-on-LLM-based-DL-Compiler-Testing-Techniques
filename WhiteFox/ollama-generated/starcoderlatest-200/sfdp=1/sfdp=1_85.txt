
class Model(torch.nn.Module):
    def __init__(self, num_queries):
        super().__init__()
        self.num_queries = num_queries
 
        self.linear = torch.nn.Linear(4, 8)
        # The following layers define the qk pattern
        self.qkv = torch.nn.Linear(128, 32)
        self.attention = torch.nn.MultiheadAttention(num_heads=8, key_dim=8)
 
    def forward(self, x):
        v1 = self.linear(x[:, None, :])
        qk = self._qk()
 
        return v1
 
    def _qk(self):
        