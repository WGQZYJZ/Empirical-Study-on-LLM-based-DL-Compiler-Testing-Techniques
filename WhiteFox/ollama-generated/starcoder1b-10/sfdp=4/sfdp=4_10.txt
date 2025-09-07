
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        qk  = x1 @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask  = torch.triu(torch.ones(qk.shape[:-2] + (1, 1)), diagonal=1) # Calculate the attention mask
        attn_weight  = torch.softmax(qk * attn_mask, dim=-1) # Apply softmax to the result
        value = self.conv(x1) @ attn_weight
        return value


# Initializing the model
m = Model()


