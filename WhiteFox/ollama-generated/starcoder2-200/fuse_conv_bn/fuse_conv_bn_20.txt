
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        return torch.nn.functional.batch_norm(input1 + 1, momentum=0) * 3

