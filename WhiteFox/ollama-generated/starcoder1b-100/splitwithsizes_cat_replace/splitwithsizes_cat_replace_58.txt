
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [1, 64]
        concatenated_tensor = []
        for i in range(len(split_sizes)):
            split_tensors = torch.split(x1, split_sizes[i], dim=2)
            concatenated_tensor.append(torch.cat(split_tensors, dim=2))
        return concatenated_tensor


# Initializing the model
m  = Model()


