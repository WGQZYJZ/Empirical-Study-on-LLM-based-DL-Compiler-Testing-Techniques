
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 5)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous()
        t1 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)

        v2 = x2.permute(0, 2, 1).contiguous()
        t2 = torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias)
        
        #t3 = torch.bmm(t1, t2)
        # or torch.matmul(t1, t2)
        #t4 = torch.bmm(t2, t1)
        # or torch.matmul(t2, t1)

        t3 = torch.bmm(x1, x2).permute(0, 2, 1, 3, 4, 5, 6, 7, 8, 9).contiguous()
        t4 = torch.bmm(t2, x1).permute(0, 2, 1, 3, 4, 5, 6, 7, 8, 9).contiguous()
        
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 4, 2)
