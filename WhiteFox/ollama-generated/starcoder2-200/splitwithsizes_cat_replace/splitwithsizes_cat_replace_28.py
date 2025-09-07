
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.norm  = torch.nn.BatchNorm2d(8)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [4], dim=1)  # Split the input tensor into two tensors of equal sizes along dimension 1 (assuming that we have three channels in our input)
        v10 = self.norm(split_tensors[0])
        v20 = split_tensors[1] + x1  # The third output is produced using an addition operation between the second and first tensors
        
        concatenated_tensor = torch.cat([v10, v20], dim=1)
 
        return concatenated_tensor

# Initializing the model with inputs
m = Model()
x1  = torch.randn(1,3*4,8,9).long() # A tensor of size (1 x 24 x 8 x 9) where each channel has three values and one batch

