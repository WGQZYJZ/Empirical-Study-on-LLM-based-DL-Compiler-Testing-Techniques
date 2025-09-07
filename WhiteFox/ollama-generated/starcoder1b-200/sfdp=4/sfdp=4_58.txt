
class Model(torch.nn.Module):
    def __init__(self, key_dim=128):
        super().__init__()
        self.layer = torch.nn.Linear(key_dim, 256)
 
    def forward(self, x, key):
        k  = torch.stack([key] * self.layer.in_features, dim=-1)
        q  = x @ k.transpose(-2, -1) / math.sqrt(k.size(-1))  # Compute the dot product of the query and key tensors
        q = q + (torch.eye(q.shape[0]) * -1e9).to(x) # Add an additional epsilon to make sure that attention weights do not become infinitely large
        attn_weight = torch.softmax(q, dim=-1)  # Compute the softmax of the dot product of the query and key
        value = x @ attn_weight
        return value


# Initializing the model
m = Model()

