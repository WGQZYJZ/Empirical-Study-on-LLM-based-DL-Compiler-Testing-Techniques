
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        split_tensor1 = torch.split(x1, [64], dim=0)  # Split the input tensor along axis 0 into two tensors: t1 and t2
        split_tensor2 = torch.split(x2, [64], dim=0)  # Split the input tensor along axis 0 into two tensors: t3 and t4
        concatenated_tensor = torch.cat([split_tensor1[i] for i in range(len(split_sizes))], dim=0)  # Concatenate the split tensors along the same dimension
        output = self.conv(concatenated_tensor)
        return output


# Initializing the model
m = Model()

