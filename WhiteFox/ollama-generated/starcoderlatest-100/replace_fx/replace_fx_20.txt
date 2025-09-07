
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        # input: [batch_size, seq_len] tensor of float
        t1 = torch.nn.functional.dropout(x1, 0.5)
        # output: [batch_size, seq_len, d_model], d_model is set in __init__
        t2 = self.linear(t1)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, dtype=torch.float)
