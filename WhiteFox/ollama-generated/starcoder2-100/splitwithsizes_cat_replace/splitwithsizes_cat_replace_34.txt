
class Model(torch.nn.Module):
    def __init__(self, n, k=2):
        super().__init__()
 
        self.conv  = torch.nn.Conv1d(n, n * k, kernel_size=3)
 
    def forward(self, input0):
        v1  = self.conv(input0).clone()
        v2  = self.conv(v1 + 1.) # Add 1 to the output of the convolution operation
        v4  = torch.split(input0, split_sizes=3 * [7], dim=2) 
        v5  = torch.cat([torch.split(v1[i], split_sizes=[k] * k)[j] for i in range(len(v1)) for j in range(k)], dim=-1).clone()
        return v4, v5

# Initializing the model
m  = Model(32)

