
class Model(torch.nn.Module):
    def __init__(self, n_head=8, d_key=64, d_value=128):
        super().__init__()
        self.scale = math.sqrt(d_key)  # Compute the sqrt of the number of head
        self.linear = torch.nn.Linear(d_key, n_head * d_key)
        self.attn_mask = torch.zeros(1, n_head).float()  # Initialize the attention mask

    def forward(self, x):
        query = self.linear(x)  # Compute the query after linear transformation
        attn_weight = torch.softmax(query @ self.scale.unsqueeze(-1), dim=-1)  # Apply softmax to the dot product of the query and the scaled matrix
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the output
        return torch.matmul(attn_weight, x), self.attn_mask


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
m1, attn_mask = m(x1)


