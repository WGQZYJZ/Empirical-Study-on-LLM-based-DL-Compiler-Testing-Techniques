class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1_t1 = x1.permute((0, 2, 1)) # Permute tensor A
        v1_t2 = x2.permute((0, 2, 1)) # Permute tensor B

        v3  = torch.bmm(v1_t1, v1_t2)

        v4  = self.linear1(torch.nn.functional.linear(self.linear2(v3)))
        return v4


m = Model()
