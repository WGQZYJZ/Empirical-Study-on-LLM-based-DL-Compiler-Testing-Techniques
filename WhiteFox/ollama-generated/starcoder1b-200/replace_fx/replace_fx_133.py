
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @torch.jit.script_method
    def forward(input_tensor, training=True):
        return input_tensor

    def train_(self, x1):
        pass


