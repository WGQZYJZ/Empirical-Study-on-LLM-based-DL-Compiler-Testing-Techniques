
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(torch.randn(3, 8, 1, stride=2, padding=1), requires_grad=True)
        self.key    = torch.nn.Parameter(torch.randn(3, 8, 1, stride=2, padding=1), requires_grad=True)
        self.value  = torch.nn.Parameter(torch.randn(3, 8, 64, 64), requires_grad=True)
        self.mask   = None
 
    def forward(self, x1):
        query = self.query  # Get the current query
        key    = self.key    # Get the current key
        value  = self.value  # Get the current value

        qk = (query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_mask = torch.bernoulli(qk)  # Add the attention mask to the scaled dot product

        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


