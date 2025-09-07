
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # pylint: disable=arguments-differ
        return torch.relu(torch.cat([x1, x2], dim=-3))


m = Model()
inputs = [
    torch.randn(40), torch.zeros((50)),
    torch.ones(60) / 8 + 2., torch.zeros(70)]
out = m(*inputs).shape
if not (out[1] == 4): exit('Invalid shape of the output: {}'.format(out))

