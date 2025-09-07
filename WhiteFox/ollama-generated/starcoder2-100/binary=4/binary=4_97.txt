
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 16)

    def forward(self, x1, y1):
        v1 = self.linear(x1 + y1) # Adding two tensors is supported by PyTorch
        return v1

m = Model()

