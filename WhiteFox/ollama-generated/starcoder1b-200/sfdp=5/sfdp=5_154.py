
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 10, bias=False)
        self.key   = torch.nn.Linear(32, 10, bias=False)
        self.value = torch.nn.Linear(10, 4, bias=False)

    def forward(self, x):
        query  = self.query(x)
        key    = self.key(x)
        value  = self.value(x)

        attn_mask = None
        # __output__ is an intermediate output of the layer, so we have to use it here too
        attn_weight = None
        for _ in range(self.num_layers):
            query  = torch.mm(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))

            if attn_mask is not None:
                attn_mask = attn_mask & (1 - self.dropout)  # [batch x length]

                if self.training and self.dropout_p != 0.0:
                    query *= torch.sigmoid(attn_weight) * (1 - self.dropout)
            else:
                attn_mask = torch.ones_like(query)

            key    = torch.mm(key, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
            value  = torch.mm(value, value.transpose(-2, -1))

            if self.training and self.dropout_p != 0.0:
                query *= torch.sigmoid(attn_weight) * (1 - self.dropout)
        return __output__


# Initializing the model
m = Model()


