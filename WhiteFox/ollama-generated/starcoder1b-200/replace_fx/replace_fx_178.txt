
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # swaps the last two dimensions of the tensor
        # This op can be replaced with `torch.dropout` by calling the method
        # replace_fx("torch.nn.functional.dropout", "lowmem_dropout")
        return v2


# Initializing the model
m = Model()
__output__  = m(x1)

