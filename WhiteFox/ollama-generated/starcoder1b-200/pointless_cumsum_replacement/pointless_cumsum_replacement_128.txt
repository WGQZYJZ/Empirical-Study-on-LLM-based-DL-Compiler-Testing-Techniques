
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.full([5, 3, 2], 0, dtype=torch.int64, device='cpu') * 1

 # Inputs to the model
x1 = torch.full([7, 8], 1, device='cuda')
