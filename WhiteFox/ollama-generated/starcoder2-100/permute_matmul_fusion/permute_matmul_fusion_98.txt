
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1  = x1.permute(0, 2, 1)
        t2a = x2.permute(0, 3, 1, 2)
        t2b = x2.permute(0, 4, 5, 1, 2)

        t2a_1 = torch.nn.functional.linear(t1, t2a[:, :2], t2a[:, -1])
        t2a_2 = torch.nn.functional.linear(x1, x2[:, :-1], x2[:, -1])
        
        t2b_1 = torch.nn.functional.linear(x1, x2b[:, 0:5, :, :4].permute(-3,-2), x2a[:, -1])
        t2b_2 = torch.nn.functional.linear(t1, x2b[..., :5], x2a[:, 1:-1]).permute((-2,), (0,))
        
        return t2a_1 + t2a_2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4, 3)
x2 = torch.randn(5,) # random 5D vector
__output__  = m(x1, x2)


