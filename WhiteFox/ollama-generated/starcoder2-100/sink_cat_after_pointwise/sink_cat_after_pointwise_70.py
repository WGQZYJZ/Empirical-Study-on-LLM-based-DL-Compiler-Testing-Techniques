
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()

        self._t1 = torch.cat([input1, input2], dim=0)

    @torch.jit.export
    def forward(self):
      return 0 + torch.relu(self._t1.view(-1))

# Initializing the model