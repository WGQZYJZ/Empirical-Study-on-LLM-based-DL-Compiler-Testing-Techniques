
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_linear = torch.nn.Linear(32, 32)
        self.output_linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1, x2):
        batch_size = x1.shape[0]
        h   = self.qkv_linear(x1).contiguous()
        h   = h.matmul(x2.transpose(-2, -1)) / math.sqrt(self.hidden_dim)
        output = self.output_linear(h)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
query = torch.randn(batch_size, query_size, num_heads)  # Query input
key = torch.randn(batch_size, key_size, num_heads)  # Key input
value = torch.randn(batch_size, value_size)  # Value input
