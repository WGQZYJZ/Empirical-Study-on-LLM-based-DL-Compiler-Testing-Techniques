
class Model(torch.nn.Module):
    def __init__(self, input_dim=2):
        super().__init__()

        self.input_dim = input_dim
        self.linear1  = torch.nn.Linear(input_dim*input_dim, input_dim)
        self.linear2  = torch.nn.Linear(input_dim, input_dim**2)

    def forward(self, input):
        v1  = input[:, 0:3] # take the first 3 columns of matrix A
        v2  = input[:, 4:] # take the remaining columns of matix B

        t1  = self.linear1(v1).permute(0, 2, 1)
        t2  = torch.bmm(t1, v2.permute(0, 2, 1))
        return self.linear2(t2.view(-1, input_dim**2))


m  = Model()
x1 = torch.rand(3, input_dim**2)
__output__= m(x1)
