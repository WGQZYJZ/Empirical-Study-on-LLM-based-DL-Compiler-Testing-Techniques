
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Dropout is supported for CPU and GPU devices as of now
        v2 = torch.rand_like(v1)
        return self.linear(v2)


# Input to the model
x1 = torch.randn(1, 2, 2)
