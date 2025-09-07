
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # swap the 1st and last dimensions of input_tensor A
        v2  = x1[0].permute(0, 2, 1) # swap the 1st and last dimensions of input_tensor B
        v3  = torch.bmm(v1 + v2, self.linear.weight) # or torch.matmul()
        return v3


m  = Model()
x1  = torch.randn(1, 4, 2)
__output__  = m(x1)