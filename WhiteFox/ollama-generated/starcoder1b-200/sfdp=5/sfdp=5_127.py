
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 4)
        self.key = torch.nn.Linear(8, 2)
        self.value = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        qk  = self.query(x1) @ self.key(x2).transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += torch.zeros_like(qk).to(x1.device)  # Add an attention mask to the scaled dot product
        attn_weight = F.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = F.dropout(attn_weight, dropout_p, training=self.training) # Apply dropout to the softmax output
        value  = self.value(attn_weight @ x2).unsqueeze(-1) # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model()


