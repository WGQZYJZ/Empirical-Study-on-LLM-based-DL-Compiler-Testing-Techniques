
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, 1, stride=1)

    def forward(self, x1, x2, query):
        