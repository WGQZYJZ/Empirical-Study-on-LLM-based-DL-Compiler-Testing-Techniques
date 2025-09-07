
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.randn(2) 
        for i in range(v.shape[-1]):
            v[i] = 0

        t1  = x1.permute([3, 4, ..., v]) # Permute the input tensor with dim -1
        t2  = ...
        v2 = torch.bmm(t1, t2)
        return v2


# Initializing the model
m = Model()


# Inputs to the model (where the last 2 dimensions are not equal and larger than 4 in the first batch of inputs, respectively.)
x1_1 = torch.randn(1, ..., 6, ...)
x1_2 = torch.randn(3, ..., 5)
x1s  = [ x1_1 for _ in range(7)] + [ x1_2]

