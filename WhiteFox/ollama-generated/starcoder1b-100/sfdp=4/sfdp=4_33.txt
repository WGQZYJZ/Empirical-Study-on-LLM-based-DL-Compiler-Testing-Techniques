
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key   = torch.nn.Linear(8, 4)
        self.value = torch.nn.Linear(128, 8)

    def forward(self, x1):
        query    = self.query(x1).reshape(-1, 4)
        key      = self.key(x1).reshape(-1, 4)
        value    = self.value(x1).reshape(-1, 8)
        attn_mask = torch.zeros(query.shape[0], query.shape[1], device=x1.device).bernoulli_(prob=0.25)  # Add the attention mask to the key and value tensors for training
        attn_weight = self._compute_softmax(attn_mask, query, key)
        output = attn_weight @ value
        return output

    def _compute_softmax(self, attn_mask, qk):
        attn_norm = torch.sqrt(torch.clamp(qk, min=1e-6))
        attn_weight = qk / attn_norm  # Compute the normalized softmax
        output = torch.exp(attn_weight)
        output /= output.sum(-1).view(-1, 1)
        return output

# Initializing the model
m = Model()


