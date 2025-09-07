
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(input_tensor, 0.5)
        t2 = torch.rand_like(input_tensor, dtype=torch.float32)
        return t1 * t2


# Inputs to the model
x1 = torch.randn(1, 2, 2).to(dtype=torch.float32)
