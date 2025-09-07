
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 32)
 
    def forward(self, x1):
        t1 = torch.norm(x1, dim=-1)
        t2 = torch.einsum('b n d, b h w e -> b h w e', t1, self.linear(x1))
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 768) # Shape: (batch_size, dim)
