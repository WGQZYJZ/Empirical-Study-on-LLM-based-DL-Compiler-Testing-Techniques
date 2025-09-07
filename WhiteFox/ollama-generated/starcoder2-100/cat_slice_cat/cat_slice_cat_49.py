
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, xs: Tuple[torch.Tensor]):
        xs = torch.cat(xs)[:, :9223372036854775807][:size]
        return torch.cat([xs, xs], dim=1)

# Initializing the model
m  = Model()

