
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 1024)
        self.key = torch.nn.Linear(3, 1024)
        self.value = torch.nn.Linear(64, 512)

    def forward(self, query_tensor, key_tensor, value_tensor):
        