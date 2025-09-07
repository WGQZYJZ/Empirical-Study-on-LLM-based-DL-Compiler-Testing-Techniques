
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *inputs: Any) -> List[torch.Tensor]:
        v1 = torch.cat(inputs, dim=1)
        v2 = v1[:, 0 : int(size)]
        return [v2]

# Initializing the model
m = Model()


# Inputs to the model
__inputs__ = (x1,)

