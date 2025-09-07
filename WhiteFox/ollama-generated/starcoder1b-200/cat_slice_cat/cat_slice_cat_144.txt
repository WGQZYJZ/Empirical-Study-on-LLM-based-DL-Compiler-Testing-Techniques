
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor):
        v1 = torch.cat([input_tensor[:, 0:9223372036854775807],
                        input_tensor[:, 9223372036854775807:]], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = torch.cat([v2,
                        input_tensor[:, 9223372036854775807:]]), dim=1)
        return torch.cat([input_tensor, v3])


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
