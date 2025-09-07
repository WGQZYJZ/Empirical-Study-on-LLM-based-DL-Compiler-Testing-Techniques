
class Attention(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
 
        self.linear = torch.nn.Linear(input_dim, hidden_dim)
 
    def forward(self, query, key, value, scale=False):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        if scale:
            return F.softmax(scaled_qk / math.sqrt(key.size()[-1]), dim=-1) * value  # Apply softmax to the scaled dot product
        else:
            return torch.matmul(F.softmax(scaled_qk, dim=-1), value) # Compute the dot product of the dropout output and the value tensor
# Initializing the model
m = Attention(64, 64)

 # Inputs to the model
x1 = torch.randn(1, 32, 512)
x2 = torch.randn(1, 8, 512)
x3 = torch.randn(1, 128, 512)
x4 = torch.randn(1, 512, 1024)
