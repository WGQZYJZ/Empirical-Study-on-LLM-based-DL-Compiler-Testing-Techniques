
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(d_model, nhead)

    def forward(self, q, k, v, attn_mask):
        attn = self.attn(q @ k.transpose(-2, -1))  # Compute the dot product of the attention weights and the key-value tensor
        attn = torch.softmax(attn, dim=-1)  # Apply softmax to the result
        attn = torch.dropout(attn, dropout_p, True)  # Apply dropout to the softmax output
        output = attn @ v  # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m = Model()


