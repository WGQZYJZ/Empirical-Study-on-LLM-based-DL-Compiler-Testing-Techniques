
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors1, _ = torch.split(x1, 4096, dim=3)
        concatenate_tensor1 = torch.cat(split_tensors1, dim=2)
        conv_tensor1 = self.conv1(concatenate_tensor1)
 
        for i in range(3):
            split_tensors2, _ = torch.split(x1, 4096, dim=3)
            concatenate_tensor2 = torch.cat([concatenate_tensor1[i], split_tensors2[i]], dim=2)
            conv_tensor2 = self.conv1(concatenate_tensor2)
 
        return conv_tensor2

# Initializing the model
m = Model()


