
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x):
        t1 = input.permute((0, 2, 1))
        t2 = torch.nn.functional.dropout(t1)

        v1 = torch.nn.functional.linear(input_tensor=t1, weight=self.linear1.weight, bias=self.linear1.bias) 
        v2 = torch.randlike(v1)
        return v2
