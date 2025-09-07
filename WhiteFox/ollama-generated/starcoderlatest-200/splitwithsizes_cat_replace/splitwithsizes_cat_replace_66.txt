
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_tensors = torch.split(input_tensor, split_sizes, dim)

    def forward(self, x1):
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        return concatenated_tensor

