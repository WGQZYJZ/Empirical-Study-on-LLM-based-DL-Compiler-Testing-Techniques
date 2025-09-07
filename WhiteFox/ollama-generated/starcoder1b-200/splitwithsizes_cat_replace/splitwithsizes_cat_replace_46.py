
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def is_valid_splitwithsizes_cat(self, split_sizes):
        if (torch.split(input_tensor, split_sizes, dim)[0].shape != self.conv.weight.shape).any() or \
            torch.cat([torch.split(split_tensors[i], split_sizes, dim)[0] for i in range(len(split_sizes))], dim) \
             .shape != input_tensor.shape:
            return False
        return True

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.split(v1, split_sizes=3, dim=-1)
        v3 = v2[0] * 0.5
        v4 = v2[1] * 0.7071067811865476
        v5 = torch.erf(v3)
        v6 = v4 + 1
        v7 = v6 * v5
        return v7


# Initializing the model
m = Model()

