
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 64)
        self.key = torch.nn.Linear(32, 64)
        self.value = torch.nn.Linear(32, 64)
 
    def forward(self, qk):
        attn_weight = torch.matmul(qk, key.transpose(-2, -1)) / math.sqrt(q1.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_weight = attn_weight + attn_mask  # Add the attention mask to the scaled dot product
        return torch.matmul(attn_weight, value)  # Compute the dot product of the dropout output and the value

# Initializing the model
m = Model()

