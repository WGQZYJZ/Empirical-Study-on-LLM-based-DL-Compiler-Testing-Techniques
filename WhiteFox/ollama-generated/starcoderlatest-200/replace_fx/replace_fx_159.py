
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x):
        t1 = torch.nn.functional.dropout(x, 0.5, training=True) # A high chance of dropout is set to True for this model instance.
        t2 = torch.rand_like(t1)
        v1 = torch.sigmoid(self.linear(t1))
        return v1
