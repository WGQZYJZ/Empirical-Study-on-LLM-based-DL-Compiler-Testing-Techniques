
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, self.linear.weight, self.linear.bias, self.linear.replace_fx, self.training, self.inplace, self.dropout, self.training)
        return v2

