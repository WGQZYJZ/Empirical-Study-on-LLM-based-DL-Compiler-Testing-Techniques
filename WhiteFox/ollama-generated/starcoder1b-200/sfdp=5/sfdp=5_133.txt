
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.attn = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, x1, x2):
        query  = self.attn(x1)
        key     = self.attn(x2)
        attn_mask = torch.zeros_like(query)
        # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(attn_mask * query / math.sqrt(key.size(-1)), dim=-1)
        # Apply dropout to the softmax output
        attn_weight = torch.dropout(attn_weight, 0.5)
        output = torch.bmm(attn_weight, x2).squeeze(-1)
        return output


# Initializing the model
m = Model()


