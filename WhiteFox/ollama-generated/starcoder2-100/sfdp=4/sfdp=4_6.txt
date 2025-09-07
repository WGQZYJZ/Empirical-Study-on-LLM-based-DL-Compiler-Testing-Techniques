
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(4, 8)
        self.key = torch.nn.Linear(32 * 16 + 32 * 32 + 80, 57)
 
    def forward(self, x1, x2):
        v1 = torch.flatten(x1.permute(0, 4, 2, 3), start_dim=1)
        v2 = self.query(v1)
 
        v3 = torch.einsum("ijl->jil", x2)
        v4 = self.key(torch.concat([v3[:, :-8], v3[:, -50:], v3[:, 57:]], dim=1))
        v5 = torch.nn.functional.softmax(
            (v2 @ v4.transpose(-2, -1).contiguous()) / math.sqrt(x1.size(-1)),
            dim=-1)
 
        return torch.einsum("jil,ijkl->ijk", [v5] * 3 + [x2], [x2])


# Initializing the model
m = Model()

# Inputs to the model
input1_ = torch.randn(80, 4, 16)
input2_ = torch.randn(37, 5, 32, 32).cuda().permute(0, 4, 2, 3)
