
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attention_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

