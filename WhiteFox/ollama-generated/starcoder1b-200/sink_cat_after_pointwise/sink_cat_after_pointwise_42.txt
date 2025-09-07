
class Model(torch.nn.Module):
    def __init__(self, input_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(input_tensor.shape[-1], 2)

    def forward(self, x1):
        v1 = torch.cat([x1[:, :-1, :], x1[..., -1:, :]], dim=-1)
        return torch.relu(self.linear(v1))


# Initializing the model
m = Model()


