
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_weight = None
 
    def forward(self, x1, x2, query):
        v2 = torch.einsum('...mnd,...md->...n', (x1, x2))  # Matrix multiplication between the first input and the second input
        attn_weight = torch.softmax(torch.einsum('...nk,...kmd->...m', (query, v2)), dim=-1)  # Compute the dot product of the query and key, and scale it

        self.attn_weight = attn_weight  # Set the output of the attention mechanism to None
        return torch.einsum('...mnd,...nkd->...md', (attn_weight, x2))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
query = torch.randn(1, 3, 64, 64)
