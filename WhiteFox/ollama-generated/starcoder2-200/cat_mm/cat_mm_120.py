class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.mm = torch.nn.Linear(input1*input2, 3)

    def forward(self, x1):
        v1  = self.mm(x1)
        v2  = torch.cat([v1] * len([v1]), dim=0).view(-1, input1, input2)
        return v2
