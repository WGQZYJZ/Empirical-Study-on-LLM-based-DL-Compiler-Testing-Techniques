
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, v438, v709, v752):
        self._v68  = v438
        self._v1033  = v709 + v752

        return torch.addmm(weight=self._v1033 * self._v68, batch1=None, batch2=None)


# Initializing the model
m = Model()

