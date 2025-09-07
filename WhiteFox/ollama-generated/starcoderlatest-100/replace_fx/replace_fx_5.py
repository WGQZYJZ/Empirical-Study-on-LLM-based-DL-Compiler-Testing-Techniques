
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Replace the node invoking dropout with a call to lowmem_dropout
        v2 = torch.rand_like(v1) # Replace the node invoking rand_like with a call to rand_like
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
