
class Model(torch.nn.Module):
    def __init__(self, num_layers=1):
        super().__init__()
        self.layer = torch.nn.Sequential(...)
        if num_layers > 0:
            self.fc1  = ...
            self.bn1  = ...
            self.relu = ...

    def forward(self, x1):
        