
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_proj = torch.nn.Linear(128, 16384) # Projections for query, key, and value
 
    def forward(self, qk1, vk1, vj1):
        query, key, value = qk1
        scaled_qk = query @ key.transpose(-2, -1) / 0.0707963
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
        output = dropout_qk @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk1 = torch.randn(2, 3, 16384).chunk(3, dim=-2) # qk: (2, 3, 3072, 128), vk: (2, 128, 3, 512), vj: (2, 512, 16, 8)
