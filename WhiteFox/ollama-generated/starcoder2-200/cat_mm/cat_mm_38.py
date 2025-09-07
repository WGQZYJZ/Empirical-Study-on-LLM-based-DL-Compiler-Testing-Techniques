

class Model(torch.nn.Module):
    def __init__(self, dims):
        super().__init__()
 
    def forward(self, x1, x2):

        def func():
            v = torch.mm(x1, x2)

            for i in range(len(dims)):
                v = torch.cat([v] * len(dims), 0)
            return v

        v = func()
        return v

# Initializing the model