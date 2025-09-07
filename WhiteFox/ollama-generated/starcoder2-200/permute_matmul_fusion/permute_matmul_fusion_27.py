
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1).view(-1, 4)
        v2  = x2.permute(0, 3, 2, 1).contiguous().view(-1, 5)

        v3  = torch.bmm(v1, v2) 
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 2, 4) # shape=(4, 2, 4), 4 is the batch size.
x2  = torch.randn(5, 2, 3) # shape=(5, 3, 2). The first 2 dimensions can be flipped to match the 1st and last dimension of t1 in forward function.

__output__  = m(x1, x2)


