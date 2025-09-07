
class Model(torch.nn.Module):
    def __init__(self, key_dim=128):
        super().__init__()
        self.query = torch.nn.Linear(3, 128)
        self.key = torch.nn.Linear(3, key_dim)
        self.value = torch.nn.Linear(key_dim, 1)

    def forward(self, query_tensor, key_tensor, value_tensor):
        qk = query_tensor @ key_tensor.transpose(-2, -1) / math.sqrt(query_tensor.size(-1))

        # Calculate the attention weights
        attn_weight = torch.softmax(qk, dim=-1)

        # Apply dropout to attention weights and compute value from them
        output = attn_weight @ value_tensor

# Initializing the model
m  = Model()

# Inputs to the model
q1 = torch.randn(1, 3, 64, 64)
k1 = torch.randn(128, 128)
v1 = torch.randn(128, 1)
