
class MyModel(torch.nn.Module):
    def __init__(self, conv1d=32) -> None:
        super().__init__()

        self._conv = torch.nn.Conv1d(500, 4096, 1)

    @torch.jit.ignore 
    def forward(self, input: Tensor):
        conv_out = torch.nn.functional.pad(input, [1])
        return torch.nn.functional.batchnorm(conv_out)

# Inputs to the model
x1 = torch.randn(2048, 500).to('cuda')

__output__  = m(x1)

