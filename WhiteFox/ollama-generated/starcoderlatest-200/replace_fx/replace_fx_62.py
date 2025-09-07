
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(input_tensor, 0.5)
        t2 = torch.rand_like(x1, x1.dtype)
        return t1 * t2


# Initialization of the model
m = Model()
