
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return self.linear(x1)

    def no_permute_ops(self): # This is a convenience to make sure that it is valid (no errors in model building).
        return torch.nn.functional.dropout(input_tensor, p=0., training=self.training)
