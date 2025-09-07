
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = v1 * clamp(min=0, max=6, v1 + 3) 
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
__input__  = torch.randn(48, 3).to_device('cuda')

__output__  = m(__input__)

assert torch.__version__.startswith('1.9'), 'The target PyTorch version should be at least v1.9.'