
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        query = self.query(x).unsqueeze(-1) # Reshape the batch and the channel dimension to fit attention mechanism
        key = self.key(x).unsqueeze(-2)
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attn_mask = (query != query).type(qk.dtype).unsqueeze(-3)
        output = qk + attn_mask # Add the attention mask to the scaled dot product
        return torch.softmax(output, dim=-1), output


# Initializing the model
m = Model()
attn_weights, 