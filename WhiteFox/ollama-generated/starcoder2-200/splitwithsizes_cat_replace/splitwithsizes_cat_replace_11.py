class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()

    def forward(self, input_tensor):
        split_tensors = torch.split(input_tensor, [8], 0)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=dim)
