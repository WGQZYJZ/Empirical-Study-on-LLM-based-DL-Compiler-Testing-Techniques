
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1: torch.Tensor[dtype=int32, device='cpu'], arg2: float32):
        