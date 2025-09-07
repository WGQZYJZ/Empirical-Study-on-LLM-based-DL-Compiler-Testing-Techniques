class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x):
        x  = self.linear1(x).dropout(0.5) 
        return x
