import torch

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        index = torch.randperm(x.shape[0], device=x.device)[:y.shape[0]]
        result = torch.index_add(x, dim=0, source=y, index=index)
        return (result, index)


x = torch.randn(10, 5)
y = torch.randn(5)

with torch.no_grad():
    func = Model()
    func = torch.compile(func)
    print(func(x.clone(), y.clone()))

func = Model().to('cpu')
print(func(x.clone(), y.clone()))