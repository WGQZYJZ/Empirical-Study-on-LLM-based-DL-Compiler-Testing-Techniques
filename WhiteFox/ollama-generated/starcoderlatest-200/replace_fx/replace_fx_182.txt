
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5) # Fallback to lowmem_dropout. 
        t2 = torch.rand_like(t1, dtype=torch.float32) # Replace rand_like with random_like
        return t2


# Inputs to the model
x1 = torch.randn(2, 4, 3)
