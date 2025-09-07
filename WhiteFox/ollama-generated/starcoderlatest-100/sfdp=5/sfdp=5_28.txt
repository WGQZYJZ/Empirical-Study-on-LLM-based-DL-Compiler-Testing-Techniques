
class Model(torch.nn.Module):
    def __init__(self, hidden_size=2048):
        super().__init__()
        self.query = torch.nn.Linear(hidden_size, hidden_size)
        self.key = torch.nn.Linear(hidden_size, hidden_size)
        self.value = torch.nn.Linear(hidden_size, hidden_size)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, self.key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + torch.abs(torch.eye(key.shape[-2]).to(qk.device).unsqueeze(dim=0) * (1e9 - 1)) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ self.value # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()
q = torch.randn(8, 2048, 64, 64)
k = torch.randn(8, 2048, 64, 64)
v = torch.randn(8, 2048, 64, 64)

