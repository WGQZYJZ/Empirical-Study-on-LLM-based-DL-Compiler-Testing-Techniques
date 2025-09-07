
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        v2 = torch.nn.functional.dropout(input1, p=0.5)
        v3 = torch.rand_like(v2, mean=27.84, stddev=9.65)
        return v3

# Initializing the model
m = Model()
__output__  = m(torch.ones((1, 10)))

