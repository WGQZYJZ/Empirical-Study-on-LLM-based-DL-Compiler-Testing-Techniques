class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(784, 500)
 
    def forward(self, x1):
        v2 = torch.nn.functional.softmax(self.l1(x1), dim=1)
        v3 = v2 * clamp(min=0, max=6, l1 + 3).relu() / 6

        return v3
