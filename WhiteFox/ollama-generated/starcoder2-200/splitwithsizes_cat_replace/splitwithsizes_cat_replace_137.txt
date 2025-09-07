
class Model(torch.nn.Module):
    def __init__(self, num_splits=5):
        super().__init__()
 
        self.split_1  = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.split_2  = torch.nn.Conv2d(8, 64, kernel_size=1)
        self.split_3  = torch.nn.Conv2d(64, 50, kernel_size=1)
 
    def forward(self, x):
        v1  = self.split_1(x)
 
        split_tensors  = torch.split(v1, [9], dim=-1)
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_tensors))], -1)
 
        v2  = self.split_2(concatenated_tensor)
        v3  = self.split_3(v2)
 
        return v3


# Initializing the model