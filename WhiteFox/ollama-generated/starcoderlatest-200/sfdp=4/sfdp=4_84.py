
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.rand(3, 8))
        self.key   = torch.nn.Parameter(torch.rand(3, 8))
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk + 0.5 * torch.eye(key.shape[0]), dim=-1)
        output = attn_weight @ self.value  # Compute the dot product of the attention weights and the value tensor
        return output

# Initializing the model
m = Model()

