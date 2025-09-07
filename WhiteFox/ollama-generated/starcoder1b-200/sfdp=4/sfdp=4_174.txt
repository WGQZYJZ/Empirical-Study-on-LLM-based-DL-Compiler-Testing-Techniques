
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 2)
        self.key = torch.nn.Linear(3, 4)
        self.value = torch.nn.Linear(3, 2)
        self.attn_mask = torch.nn.Parameter(torch.ones((1, 2)))
 
    def forward(self, x1, x2):
        qk = self.query(x1).transpose(-2, -1) @ self.key(x2).reshape(1, 4, -1) / math.sqrt(self.key.weight.size(0))  # Compute the dot product of the query and key, and scale it
        qk = qk + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ self.value(x2).reshape(1, 2, -1)  # Compute the dot product of the attention weights and the value
        return output


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 3, 64, 64)
