

class Model(torch.nn.Module):
    def __init__(self, num_features: int) -> None
        self.linear = torch.nn.Linear(num_features, 1024 + 256 * 3)
    
    def forward(self, x: torch.Tensor):
        t1 = torch.relu(x.view(-1, 1))
        return t1


class Model2(torch.nn.Module):
    def __init__(self, num_features: int) -> None
        self.linear = torch.nn.Linear(num_features + 5096, 784 + 3 * 256)
    
    def forward(self, x: torch.Tensor):
        t1 = torch.relu(x.view(-1, 1)) # Permute
        return t1
