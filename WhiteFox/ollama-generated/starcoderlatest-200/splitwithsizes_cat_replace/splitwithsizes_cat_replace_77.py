
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [64, 64], dim=0) # Split the input tensor into two tensors along dimension 0
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(2)], dim=0) # Concatenate split tensors along the same dimension
        return x1
    
# Initializing the model
m = Model()


