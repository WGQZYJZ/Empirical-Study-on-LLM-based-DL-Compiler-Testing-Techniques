
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return attn_mask * output + (1 - attn_mask) * mask


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 64, 64)
mask = torch.zeros(1, 3, 64, 64).bool()


# Forward propagation of the model
