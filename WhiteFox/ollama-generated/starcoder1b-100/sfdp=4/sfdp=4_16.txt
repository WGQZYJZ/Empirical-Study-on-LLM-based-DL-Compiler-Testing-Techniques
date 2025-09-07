
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 4)
        self.key = torch.nn.Linear(32, 4)
        self.value = torch.nn.Linear(64, 4)
        self.scale_factor = torch.sqrt(torch.FloatTensor([1 / 16, 1 / 8]))

    def forward(self, x1):
        query = self.query(x1)
        key = self.key(x1)
        value = self.value(x1)

        qk = torch.mm(query, key.transpose(-2, -1))
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result

        scale = self.scale_factor * attn_weight
        output = attn_weight @ value + (attn_mask / scale).unsqueeze(-1)  # Compute weighted sum

        return output


# Initializing the model
m = Model()


