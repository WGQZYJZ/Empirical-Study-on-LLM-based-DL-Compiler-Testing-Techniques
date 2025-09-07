
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [v1.shape[0], x1.shape[0]]
        concatenated_tensor = torch.cat([torch.split(v1, split_sizes, 0),  # Concatenate the two split tensors along dimension=0
                                        torch.split(v1, split_sizes, 1)], dim=0)  # Concatenate the two split tensors along dimension=1
        return concatenated_tensor
