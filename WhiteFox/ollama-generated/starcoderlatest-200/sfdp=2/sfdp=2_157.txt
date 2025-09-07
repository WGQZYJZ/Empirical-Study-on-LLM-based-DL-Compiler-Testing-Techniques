
class Model(torch.nn.Module):
    def __init__(self, num_heads: int = 8, head_dim: int = 64, num_buckets: int = 1024):
        super().__init__()
        self.query = torch.nn.Linear(3, head_dim)
        self.key   = torch.nn.Linear(3, head_dim)
        self.value = torch.nn.Linear(3, head_dim)
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, x1):
        query  = self.query(x1).view(-1, num_heads, -1)
        key    = self.key(x1).view(-1, num_heads, -1)
        value  = self.value(x1).view(-1, num_heads, -1)
 
        qk     = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        output = dropout_qk.matmul(value)
        return output
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
