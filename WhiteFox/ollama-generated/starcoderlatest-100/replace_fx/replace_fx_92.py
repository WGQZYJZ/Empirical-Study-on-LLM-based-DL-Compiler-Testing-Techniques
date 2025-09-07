
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # use replace_fx to change this node
        v2 = torch.rand_like(v1)                      # not replaced here
        return v2


# Initializing the model
m = Model()

