
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        with torch.no_grad():
            v1 = x1.permute(0, 2, 1)
            v2 = lowmem_dropout(input=v1, p=0.5)
            # v2 = torch.rand_like(v1, dtype=torch.float32, device='cpu')
        return v2


# Initializing the model
m = Model()
