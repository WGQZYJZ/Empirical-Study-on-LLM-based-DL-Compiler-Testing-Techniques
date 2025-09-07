
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(768, 1024)
        self.linear_k = torch.nn.Linear(768, 1024)
        self.attn_mask = torch.eye(1024).unsqueeze(dim=0)

    def forward(self, x):
        query = self.linear_q(x)
        key = self.linear_k(x)
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk + self.attn_mask, dim=-1)
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output
