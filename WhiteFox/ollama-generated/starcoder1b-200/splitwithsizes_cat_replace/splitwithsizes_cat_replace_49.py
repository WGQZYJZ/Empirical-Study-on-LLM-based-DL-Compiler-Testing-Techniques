
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [x1.shape[0] // 2, x1.shape[0] - x1.shape[0] // 2]
        concatenated_tensor = torch.cat([
            torch.split(input_tensor, split_sizes, dim)[i] for i in range(len(split_sizes))], dim)
        v1 = self.conv(concatenated_tensor)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

