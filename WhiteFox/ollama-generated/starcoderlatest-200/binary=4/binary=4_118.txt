
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*16*2, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, self.num_flat_features))
        return v1
 
class ModelWithKeywordArguments(torch.nn.Module):
    