
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1: torch.Tensor, input2: torch.Tensor) -> torch.Tensor:
        v = torch.cat([input1[:, 0].view(-1), input2], dim=0).view(-1, 4)
        return F.tanh(v)


# Initializing the model
model = Model()


# Input tensors for the model
input1 = torch.zeros((3,), dtype=torch.float32)
input2 = torch.zeros((2,), dtype=torch.float32)



