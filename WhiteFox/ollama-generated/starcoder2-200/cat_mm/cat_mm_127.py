
class Model(torch.nn.Module):
    def __init__(self, input1=torch.ones(320), input2=torch.ones(480)):
        super().__init__()
        self.mm = torch.ops.aten.mm.default(input1, input2)

    def forward(self):
        v1 = torch.ops.aten._cat_intlist(self.mm, 1, 3)
        return v1


# Initializing the model