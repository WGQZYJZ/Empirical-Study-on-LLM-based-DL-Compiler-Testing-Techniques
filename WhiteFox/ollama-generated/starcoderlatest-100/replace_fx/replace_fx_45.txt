
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, self.dropout)  # Dropout operation at the entry of model
        t2 = torch.rand_like(t1)                             # Random number generation in the middle of the model
        return t1

# Initializing the model
m2 = Model2()

