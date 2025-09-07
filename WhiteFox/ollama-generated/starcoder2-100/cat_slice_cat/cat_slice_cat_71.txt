
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *inputs):
        self.size = inputs[0].shape[-2]
        v1 = torch.cat(inputs)
        v2  = v1[:, :9223372036854775807]
        v3  = v2[:self.size, :]
 
        # Concatenation along dimension 1
        return torch.cat([v1, v3], dim=1)

# Initializing the model