
class Model(torch.nn.Module):
    def __init__(self, mlp_dim=128):
        super().__init__()
        self.mlp = torch.nn.Sequential(
            torch.nn.Linear(query_size, hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, num_attn_heads),
            torch.nn.Softmax(dim=-1)
        )

    def forward(self, query, key, value):
        k = self.mlp(key) # Compute the attention weights
        # Apply dropout to compute the output (for multi-head attention):
        attn = torch.bmm(attn_mask * k, value)
        # Compute the dot product of the two outputs:
        attn = attn @ output # The softmax function multiplies the output by the corresponding weight.
        return attn

# Initializing the model
m = Model()

