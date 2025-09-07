
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # input_tensor1
        return torch.relu(torch.cat([x1], dim=2).view(-1, 1))

