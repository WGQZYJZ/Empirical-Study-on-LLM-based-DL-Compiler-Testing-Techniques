
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 8)
        self.key   = torch.nn.Linear(64, 8)
 
    def forward(self, q1, k1):
        q2 = self.query(q1)
        k2 = self.key(k1)

        v2 = (q2 @ k2.transpose(-2, -1)) / math.sqrt(q2.size(-1))
        attn_mask = torch.eye(q2.shape[0], dtype=torch.float).unsqueeze(dim=-1)  # Create a diagonal attention mask

        output = v2 + (attn_mask * (-2e4))  # Add the value with the softmax-scaled dot product attention weight
        return output


# Inputs to the model
q1 = torch.randn(64, 3, 64, 64)
k1 = torch.randn(64, 8, 64, 64)
v1 = q1 @ k1.transpose(-2, -1) / math.sqrt(q1.size(-1)) + (torch.eye(q1.shape[0], dtype=torch.float).unsqueeze(dim=-1) * (-2e4))
