
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 8, 1) 
        self.conv2  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        split_tensors  = torch.split(x1, [int(64/2), int(64/2)], dim=0)
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0) 
        return self.conv1(self.conv2(concatenated_tensor))


# Initializing the model