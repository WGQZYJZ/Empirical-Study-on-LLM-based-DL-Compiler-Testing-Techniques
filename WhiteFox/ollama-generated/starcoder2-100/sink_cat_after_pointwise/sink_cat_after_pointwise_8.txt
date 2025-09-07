
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1: torch.Tensor) -> torch.Tensor:  # pylint: disable=unused-variable
        v1 = t1.view(-1, 256).clone()
        v2 = torch.relu_(v1)
        v3 = torch.cat([torch.ones_like(v2),
                         torch.zeros((v2.size()[0],
                                      v2.size()[1] + 1))], -1)

        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
 x1: torch.Tensor  = torch.randn(4, 5, 8, 8).clone()
 __output__: torch.Tensor = m(x1)

