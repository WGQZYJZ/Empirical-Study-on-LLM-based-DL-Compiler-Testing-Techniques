
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...) # This node will be replaced by gm.graph.add_function() call
        ...
m = Model().to('cuda:0')

