
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor):
        x1 = torch.randn(2, 1, *input_tensor.shape[-2:])
        x2 = input_tensor[:, 0:9223372036854775807]
        x3 = x2[:, 0:128]
        return torch.cat([x1, x3], dim=1)


# Initializing the model
m = Model()


