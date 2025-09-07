
class Model(torch.nn.Module):
    def __init__(self, dropout=False, replace_fx=True, fallback_random=True):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    @torch.jit.script_method
    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        # ...
