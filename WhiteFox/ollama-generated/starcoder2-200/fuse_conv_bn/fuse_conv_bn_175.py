
class Model(torch.nn.Module):
    def __init__(self, num_layers=200):
        super().__init__()
        self.convs = nn.Sequential(
            *[nn.Conv1d(784, 32 * (i + 1), 5) for i in range(num_layers)]
        )

    def forward(self, x):
        out = self.convs[0](x).reshape(-1, 6 * 398) # Flatten the output of the first conv layer to match with the size of input tensor.
        for idx, conv in enumerate(self.convs[1:]):
            out += nn.functional.batch_norm(conv(out))
        return out

m = Model()
x  = torch.randn(2048, 784)
out = m(x)

