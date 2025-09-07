
class Model(torch.nn.Module):
    def __init__(self, in_features, hid_size, nhead):
        super().__init__()
        self.qkv = torch.nn.Linear(in_features, hid_size * 3, bias=False)
        self.o1   = torch.nn.Linear(hid_size, hid_size, bias=False)
        self.o2   = torch.nn.Linear(hid_size, hid_size, bias=False)
        self.o3   = torch.nn.Linear(hid_size, hid_size, bias=False)

    def forward(self, x):
        k = self.qkv(x).chunk(2, dim=-1)  # (b, n_head, n_dim, dim)
        v = self.o3(self.o2(self.o1(x)))
        o1 = torch.cat([i[0] for i in k], dim=-2)  # (b, n_head * 3, n_dim, dim)
        o2 = torch.cat([i[1] for i in k], dim=-2)  # (b, n_head * 3, n_dim, dim)
        return o2


# Initializing the model
m = Model(512, 4096, 8)


