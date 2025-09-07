
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5) 
        v3 = torch.rand_like(v1) + self.linear(v1) # Adding to this line a call to 'lowmem_dropout' will not trigger the erase node code
        return x2


# Initializing the model