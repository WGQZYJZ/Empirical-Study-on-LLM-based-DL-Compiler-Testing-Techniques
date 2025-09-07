
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 1024)
        self.key = torch.nn.Linear(768, 1024)
        self.value = torch.nn.Linear(768, 1024)
        self.attn_mask = torch.nn.Linear(768, 1)
 
    def forward(self, query, key, value):
        # Compute the attention weights
        attn = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + self.attn_mask * 0
        # Normalize the attention weights
        scale = torch.sum(attn, dim=-1)
        attention = torch.div(attn, scale[:, None])  # Compute a weighted sum of value tensor
        # Apply the softmax function on the attention weights to get the output
        out = torch.softmax(attention, dim=-1) * value
        return out


# Initializing the model
m  = Model()


# Inputs to the model
query = torch.randn(5, 768)
key = torch.randn(3, 768)
value = torch.randn(2, 768)
