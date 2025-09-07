
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_weight = torch.nn.Parameter(
            torch.randn(512, 32), requires_grad=False)
        self.query = torch.nn.Parameter(torch.randn(
            512, 64, 8, 8), requires_grad=True)
 
    def forward(self, query, key):
        v = torch.einsum('b i h j, b j d e -> bi de', (
            self.attn_weight * query, key))  # Compute the dot product of the attention weights and the value
        return v


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(16, 512, 8, 8)
key   = torch.randn(16, 32, 64, 64)
