class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()

        self.num_heads  = num_heads

    @property
    def head_dim(self):
        return self.in_features // self.num_heads


    def forward(self, x1):
        assert self.head_dim > 0


        v3 = torch.nn.functional.linear(x1, self.linear.weight[:self.head_dim], self.linear.bias)

        return v3


m = Model()
