
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = torch.stack((v1[:, 0:9223372036854775807],  # slice along dimension 1
                          v1[:, 9223372036854775807:]))  # slice along dimension 1
        return torch.cat([x1, v2])


# Inputs to the model
input_tensor1 = torch.randn(1, 3, 64, 64)
input_tensor2 = torch.randn(1, 100)
