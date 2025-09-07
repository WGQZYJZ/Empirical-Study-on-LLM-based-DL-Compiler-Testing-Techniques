
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.25) 
        t2 = torch.rand_like(t1, dtype=torch.float) # dtype should not be specified here for inference to succeed
        return t2
# Inputs to the model
__input__ = torch.randn(8, 2, 3, requires_grad=True)
m = Model()
