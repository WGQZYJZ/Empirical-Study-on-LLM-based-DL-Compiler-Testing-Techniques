
class Model(torch.nn.Module):
    def __init__(self, args):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [args.feature_map_sizes[0], (x1.shape[0] + 1) // args.num_sub_groups - 1] # [input_height, num_sub_groups_without_one]
        concatenated_tensor  = torch.cat([torch.split(x1, split_sizes, dim=1)[i] for i in range(len(split_sizes))], dim=1)
        return self.conv(concatenated_tensor)


# Initializing the model
m = Model(...)
...

