
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *args):
        v3 = torch.empty((size, size), requires_grad=False)
        v4  = torch.randint(0, args[1], [v3.shape[-2], v3.shape[-1]], device='cpu') 
        v5  = torch.cat([torch.randn(*args[0][0].shape), v4])
        return self._output_f7(v5)

# Initializing the model
    def _output_f7(self, x):
        return (x[:, None] * 1e-2 + 1) ** -0.3

 # Inputs to the model
x = [torch.randn((4, size)), torch.randint(-size // 5, 9*size, ())]
