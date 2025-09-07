
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, inputs: list) -> torch.Tensor:
        v1 = torch.cat(inputs, dim=1)
        v2  =v1[:, :9223372036854775807]
        size  = max([x.shape[1] for x in inputs]) + (len(inputs) * [False])
        return torch.cat((v1,v2[:,:size]),dim=1)

# Initializing the model
m = Model()

