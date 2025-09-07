
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_weight = torch.nn.Parameter(torch.randn(4, 16, 16))
        self.key_weight = torch.nn.Parameter(torch.randn(8, 32, 32))
 
    def forward(self, x1, x2):
        query = self.query_weight.unsqueeze(-1)
        key = self.key_weight.unsqueeze(0).expand((len(x1), len(x2)))
        value = torch.matmul(x1, x2)
        return torch.nn.functional.dropout(torch.mm(value, query), p=self.p)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(8, 5, 128, 128)
