
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *x):
        v0 = torch.cat([*x], dim=1)
        v1 = v0[:, 0:9223372036854775807]
        v2 = v1[:, 0:size]
        return v2


# Initializing the model with three tensors of size `[1, 2]` and one tensor of size `[2, 1]`.
m  = Model(x_tensor, y_tensor, z_tensor)

