
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size):
        v1 = torch.cat([x1, torch.full_like(x1, fill_value=0)], dim=1) # Concatenate input tensor with a zero-valued tensor of the same shape as the input tensor
        v2 = v1[:, 0:size] # Slice the concatenated tensor along dimension 1
        v3 = torch.cat([v1, v2], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v3
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 64, 64)
size = x1.shape[0] * x1.shape[1] * x1.shape[2] * x1.shape[3] * x1.shape[4]
