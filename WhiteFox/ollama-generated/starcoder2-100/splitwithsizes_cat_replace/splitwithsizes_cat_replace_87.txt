
class Model(torch.nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.split_tensors = torch.split(input_tensor, 3)
 
    def forward(self, x1):
        concatenated_tensor = torch.cat([self.split_tensors[i] for i in range(len(split_sizes))], dim=0)
