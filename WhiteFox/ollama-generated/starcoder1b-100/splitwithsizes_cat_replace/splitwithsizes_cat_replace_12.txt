
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [1, 5]
        concatenated_tensor = torch.cat([torch.split(input_tensor, split_sizes[i], dim)[i] for i in range(len(split_sizes))], dim)
        return True if is_valid_splitwithsizes_cat(concatenated_tensor) else False


