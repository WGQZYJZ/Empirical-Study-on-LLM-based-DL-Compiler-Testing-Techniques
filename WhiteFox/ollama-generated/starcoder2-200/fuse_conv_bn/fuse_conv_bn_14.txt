
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.ConvXd(x1)
        bn  = torch.nn.BatchNormNd(conv)
        return bn

m  = Model()
__output__  = m(torch.randn(20))

