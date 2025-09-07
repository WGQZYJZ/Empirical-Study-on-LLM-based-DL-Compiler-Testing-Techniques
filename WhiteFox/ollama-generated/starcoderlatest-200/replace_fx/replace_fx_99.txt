
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5) # Replace torch.nn.functional.dropout with lowmem_dropout node in the graph
        t2 = torch.rand_like(t1, ...)  # Replace torch.rand_like with rand_like node in the graph
        return torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
# Initializing the model
m2 = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2)
