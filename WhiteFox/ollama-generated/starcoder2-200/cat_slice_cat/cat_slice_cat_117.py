
class Model(torch.nn.Module):
    def __init__(self, size: int):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.cat([x] * 2)
        v3 = torch.randint(-9223372036854775808 + (size // 2), size - 9223372036854775807, [1]) + x[0]
        v4 = torch.randint(-9223372036854775808 + (size // 2), size - 9223372036854775807, [1]) + x[1]
        v5 = torch.cat([v1, v3], dim=1)
        v6 = torch.randint(-9223372036854775808 + (size // 2), size - 9223372036854775807, [1]) + x[2]
        v7 = torch.cat([v5, v6], dim=1)
        return v7


# Initializing the model
m = Model(size)


# Inputs to the model
x  = torch.randperm(3)[0:size]
