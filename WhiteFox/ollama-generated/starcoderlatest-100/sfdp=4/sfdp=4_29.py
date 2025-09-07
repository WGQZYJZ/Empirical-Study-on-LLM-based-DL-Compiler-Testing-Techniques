
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 64)
        self.key = torch.nn.Linear(1024, 64)
        self.value = torch.nn.Linear(656, 64)
 
    def forward(self, query):
        # Apply linear layer on query to generate the key tensor
        qk = self.query(query).unsqueeze(-1)

        # Apply linear layer on key and transpose it as attention mask for queries in this position
        attn_mask = self.key(qk) @ torch.transpose(self.value, 0, 1)

        # Compute the scaled dot product of query and key, add the attention mask to them, and apply softmax to get attention weights
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)

        # Apply linear layer on value and compute the weighted sum of query and key with corresponding attention weights
        output = self.value(attn_weight).squeeze(-1) @ torch.transpose(self.key, 0, 1)
        return output


# Inputs to the model
query = torch.randn(256, 3)
