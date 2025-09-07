
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 32)
 
    def forward(self, q1, k1):
        attn_mask = torch.randn(q1.shape[0], q1.shape[1]) < -0.5
        v1 = torch.einsum("bhid,bihd->bhij", [q1, k1.transpose(-2, -1)]) / math.sqrt(k1.size(-1))
        v1 = v1 + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(v1, dim=-1)
        output = torch.einsum("bhij,bjih->bhid", [attn_weight, v1])  # Compute the weighted sum of the value tensor
        return output


# Initializing the model
m = Model()
q1 = torch.randn(20, 8)
k1 = torch.randn(20, 32)
