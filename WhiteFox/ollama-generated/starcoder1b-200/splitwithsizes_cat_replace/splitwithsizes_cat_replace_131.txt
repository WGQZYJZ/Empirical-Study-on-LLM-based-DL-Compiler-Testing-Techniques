
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    @is_valid_splitwithsizes_cat()
    def forward(self, x1, split_tensor_1):  # `split_tensor_1` is the 0-th element of `torch.split`
        v1 = self.conv(x1) * split_tensor_1

        v2 = v1 * 0.5  # Multiply `v1` by 0.5
        
        v3 = v1 * 0.7071067811865476  # Multiply `v1` by 0.7071067811865476
        v4 = torch.erf(v3)  # Apply the error function to `v3`

        v5 = v4 + 1  # Add 1 to the output of the error function
        v6 = v2 * v5  # Multiply `v2` by `v5`
        
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
split_tensor_1 = 0.2
