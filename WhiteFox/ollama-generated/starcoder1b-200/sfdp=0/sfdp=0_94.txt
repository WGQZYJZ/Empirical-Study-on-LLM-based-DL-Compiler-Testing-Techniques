
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key   = torch.nn.Linear(3, 5)
        self.value = torch.nn.Linear(3, 7)

    def forward(self, x1, x2):
        query  = self.query(x1)
        key    = self.key(x2)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (math.sqrt(self.attention_scale) * math.sqrt(self.attention_scale))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        value   = self.value(x1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m  = Model()


