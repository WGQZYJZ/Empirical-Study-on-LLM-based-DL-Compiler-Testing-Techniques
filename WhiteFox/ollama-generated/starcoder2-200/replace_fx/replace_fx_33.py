

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):

        t1 = torch.nn.functional.dropout(x1, 0.5) # This will be replaced with lowmem_dropout

        t2 = torch.nn.functional.conv3d(t1, self.linear.weight, bias=None, padding=(0, 0, 0), dilation=(1, 1, 1), stride=(1, 1, 1))
        return x1

m  = Model()

x1 = torch.randn(1, 32)

