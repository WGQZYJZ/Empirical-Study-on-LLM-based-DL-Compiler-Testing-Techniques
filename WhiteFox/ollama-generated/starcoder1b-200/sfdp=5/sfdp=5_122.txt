
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 128)
        self.key   = torch.nn.Linear(3072, 64)
        self.value = torch.nn.Linear(3072, 256)

        self.dropout_p = 0.0  # Dropout probability

    def forward(self, x):
        query = self.query(x)
        key   = self.key(x)
        value = self.value(x)
        dropout_mask = (1 - torch.softmax(query / math.sqrt(query.size(-1)), dim=-1)) * 0.25

        attn = torch.bmm(query, key.transpose(-2, -1))
        attn *= dropout_mask
        attn = attn + 0.25
        attn = torch.softmax(attn, dim=-1)
        attn = torch.dropout(attn, self.dropout_p, True)

        value = torch.bmm(attn, value)
        return value


# Initializing the model
m = Model()

