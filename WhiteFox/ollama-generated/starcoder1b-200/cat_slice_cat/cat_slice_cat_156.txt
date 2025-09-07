
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        x0 = torch.randn((1, 2, 64, 64), dtype=input_tensor.dtype)

        if hasattr(input_tensor, "shape"):
            size = input_tensor.shape[1]
            # The output of the concatenation is concatenated along dimension 1, so the output of slice and another slice are taken along dimension 1
            x1 = input_tensor[:, :, 0:size]
            x2 = input_tensor[:, :, 9223372036854775807:]
        else:
            # The output of the concatenation is concatenated along dimension 1, so the output of slice and another slice are taken along dimension 1
            size = torch.size(input_tensor)
            x1 = input_tensor[:, :, :, 0:size]
            x2 = input_tensor[:, :, :, 9223372036854775807:]

        y1, y2 = self._conv(x1, x2)
        z1, z2 = torch.cat([y1, y2], dim=1), torch.cat([x1, x2], dim=1)

        return z1, z2

    def _conv(self, x1, x2):
        w = torch.randn((1, 3, 64, 64))
        b = torch.randn((1, 3), requires_grad=True)
        v1 = x1 * w + b
        v2 = torch.exp(v1)
        v3 = v2 / torch.sum(torch.abs(v2), dim=[-2, -1])
        return v3[0], v3[1]


# Initializing the model
m = Model()


