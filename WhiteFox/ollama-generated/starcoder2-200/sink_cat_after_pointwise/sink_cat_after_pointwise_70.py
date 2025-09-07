
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1: torch.Tensor, input2: torch.Tensor) -> torch.Tensor:
        output = torch.cat([input1, input2])
        output = output.view(-1, 50).relu() # 4 -> 50
        return output


# Initializing the model
m = Model()

