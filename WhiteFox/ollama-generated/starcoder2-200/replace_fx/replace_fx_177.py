
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       t3 = torch.rand_like(x1, dtype=torch.float64)
       t2  = torch.nn.functional.dropout(t3, 0.5).to('cpu')  # Replace the call to dropout with lowmem_dropout
       return t2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 4) + m.weight * -torch.randint(-30, 30, (2, 4)) # The weight is added to make the model non-constant for this test case.
__output__  = m(x1)

